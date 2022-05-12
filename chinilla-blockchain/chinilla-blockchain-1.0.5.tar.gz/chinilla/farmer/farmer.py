import asyncio
import json
import logging
import time
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple
import traceback

import aiohttp
from blspy import AugSchemeMPL, G1Element, G2Element, PrivateKey

import chinilla.server.ws_connection as ws  # lgtm [py/import-and-import-from]
from chinilla.consensus.coinbase import create_puzzlehash_for_pk
from chinilla.consensus.constants import ConsensusConstants
from chinilla.daemon.keychain_proxy import (
    KeychainProxy,
    KeychainProxyConnectionFailure,
    connect_to_keychain_and_validate,
    wrap_local_keychain,
)
from chinilla.plot_sync.receiver import Receiver
from chinilla.plot_sync.delta import Delta
from chinilla.pools.pool_config import PoolWalletConfig, load_pool_config, add_auth_key
from chinilla.protocols import farmer_protocol, harvester_protocol
from chinilla.protocols.pool_protocol import (
    ErrorResponse,
    get_current_authentication_token,
    GetFarmerResponse,
    PoolErrorCode,
    PostFarmerPayload,
    PostFarmerRequest,
    PutFarmerPayload,
    PutFarmerRequest,
    AuthenticationPayload,
)
from chinilla.protocols.protocol_message_types import ProtocolMessageTypes
from chinilla.server.outbound_message import NodeType, make_msg
from chinilla.server.server import ssl_context_for_root
from chinilla.server.ws_connection import WSChinillaConnection
from chinilla.ssl.create_ssl import get_mozilla_ca_crt
from chinilla.types.blockchain_format.proof_of_space import ProofOfSpace
from chinilla.types.blockchain_format.sized_bytes import bytes32
from chinilla.util.bech32m import decode_puzzle_hash
from chinilla.util.byte_types import hexstr_to_bytes
from chinilla.util.config import load_config, lock_and_load_config, save_config, config_path_for_filename
from chinilla.util.hash import std_hash
from chinilla.util.ints import uint8, uint16, uint32, uint64
from chinilla.util.keychain import Keychain
from chinilla.wallet.derive_keys import (
    master_sk_to_farmer_sk,
    master_sk_to_pool_sk,
    master_sk_to_wallet_sk,
    find_authentication_sk,
    find_owner_sk,
)
from chinilla.wallet.puzzles.singleton_top_layer import SINGLETON_MOD

singleton_mod_hash = SINGLETON_MOD.get_tree_hash()

log = logging.getLogger(__name__)

UPDATE_POOL_INFO_INTERVAL: int = 3600
UPDATE_POOL_FARMER_INFO_INTERVAL: int = 300

"""
HARVESTER PROTOCOL (FARMER <-> HARVESTER)
"""


class Farmer:
    def __init__(
        self,
        root_path: Path,
        farmer_config: Dict,
        pool_config: Dict,
        consensus_constants: ConsensusConstants,
        local_keychain: Optional[Keychain] = None,
    ):
        self.keychain_proxy: Optional[KeychainProxy] = None
        self.local_keychain = local_keychain
        self._root_path = root_path
        self.config = farmer_config
        self.pool_config = pool_config
        # Keep track of all sps, keyed on challenge chain signage point hash
        self.sps: Dict[bytes32, List[farmer_protocol.NewSignagePoint]] = {}

        # Keep track of harvester plot identifier (str), target sp index, and PoSpace for each challenge
        self.proofs_of_space: Dict[bytes32, List[Tuple[str, ProofOfSpace]]] = {}

        # Quality string to plot identifier and challenge_hash, for use with harvester.RequestSignatures
        self.quality_str_to_identifiers: Dict[bytes32, Tuple[str, bytes32, bytes32, bytes32]] = {}

        # number of responses to each signage point
        self.number_of_responses: Dict[bytes32, int] = {}

        # A dictionary of keys to time added. These keys refer to keys in the above 4 dictionaries. This is used
        # to periodically clear the memory
        self.cache_add_time: Dict[bytes32, uint64] = {}

        self.plot_sync_receivers: Dict[bytes32, Receiver] = {}

        self.cache_clear_task: Optional[asyncio.Task] = None
        self.update_pool_state_task: Optional[asyncio.Task] = None
        self.constants = consensus_constants
        self._shut_down = False
        self.server: Any = None
        self.state_changed_callback: Optional[Callable] = None
        self.log = log
        self.started = False
        self.harvester_handshake_task: Optional[asyncio.Task] = None

        # From p2_singleton_puzzle_hash to pool state dict
        self.pool_state: Dict[bytes32, Dict] = {}

        # From p2_singleton to auth PrivateKey
        self.authentication_keys: Dict[bytes32, PrivateKey] = {}

        # Last time we updated pool_state based on the config file
        self.last_config_access_time: uint64 = uint64(0)

    async def ensure_keychain_proxy(self) -> KeychainProxy:
        if self.keychain_proxy is None:
            if self.local_keychain:
                self.keychain_proxy = wrap_local_keychain(self.local_keychain, log=self.log)
            else:
                self.keychain_proxy = await connect_to_keychain_and_validate(self._root_path, self.log)
                if not self.keychain_proxy:
                    raise KeychainProxyConnectionFailure("Failed to connect to keychain service")
        return self.keychain_proxy

    async def get_all_private_keys(self):
        keychain_proxy = await self.ensure_keychain_proxy()
        return await keychain_proxy.get_all_private_keys()

    async def setup_keys(self) -> bool:
        no_keys_error_str = "No keys exist. Please run 'chinilla keys generate' or open the UI."
        self.all_root_sks: List[PrivateKey] = [sk for sk, _ in await self.get_all_private_keys()]
        self._private_keys = [master_sk_to_farmer_sk(sk) for sk in self.all_root_sks] + [
            master_sk_to_pool_sk(sk) for sk in self.all_root_sks
        ]

        if len(self.get_public_keys()) == 0:
            log.warning(no_keys_error_str)
            return False

        config = load_config(self._root_path, "config.yaml")
        if "hcx_target_address" not in self.config:
            self.config = config["farmer"]
        if "hcx_target_address" not in self.pool_config:
            self.pool_config = config["pool"]
        if "hcx_target_address" not in self.config or "hcx_target_address" not in self.pool_config:
            log.debug("hcx_target_address missing in the config")
            return False

        # This is the farmer configuration
        self.farmer_target_encoded = self.config["hcx_target_address"]
        self.farmer_target = decode_puzzle_hash(self.farmer_target_encoded)

        self.pool_public_keys = [G1Element.from_bytes(bytes.fromhex(pk)) for pk in self.config["pool_public_keys"]]

        # This is the self pooling configuration, which is only used for original self-pooled plots
        self.pool_target_encoded = self.pool_config["hcx_target_address"]
        self.pool_target = decode_puzzle_hash(self.pool_target_encoded)
        self.pool_sks_map: Dict = {}
        for key in self.get_private_keys():
            self.pool_sks_map[bytes(key.get_g1())] = key

        assert len(self.farmer_target) == 32
        assert len(self.pool_target) == 32
        if len(self.pool_sks_map) == 0:
            log.warning(no_keys_error_str)
            return False

        return True

    async def _start(self):
        async def start_task():
            # `Farmer.setup_keys` returns `False` if there are no keys setup yet. In this case we just try until it
            # succeeds or until we need to shut down.
            while not self._shut_down:
                if await self.setup_keys():
                    self.update_pool_state_task = asyncio.create_task(self._periodically_update_pool_state_task())
                    self.cache_clear_task = asyncio.create_task(self._periodically_clear_cache_and_refresh_task())
                    log.debug("start_task: initialized")
                    self.started = True
                    return
                await asyncio.sleep(1)

        asyncio.create_task(start_task())

    def _close(self):
        self._shut_down = True

    async def _await_closed(self, shutting_down: bool = True):
        if self.cache_clear_task is not None:
            await self.cache_clear_task
        if self.update_pool_state_task is not None:
            await self.update_pool_state_task
        if shutting_down and self.keychain_proxy is not None:
            proxy = self.keychain_proxy
            self.keychain_proxy = None
            await proxy.close()
            await asyncio.sleep(0.5)  # https://docs.aiohttp.org/en/stable/client_advanced.html#graceful-shutdown
        self.started = False

    def _set_state_changed_callback(self, callback: Callable):
        self.state_changed_callback = callback

    async def on_connect(self, peer: WSChinillaConnection):
        self.state_changed("add_connection", {})

        async def handshake_task():
            # Wait until the task in `Farmer._start` is done so that we have keys available for the handshake. Bail out
            # early if we need to shut down or if the harvester is not longer connected.
            while not self.started and not self._shut_down and peer in self.server.get_connections():
                await asyncio.sleep(1)

            if self._shut_down:
                log.debug("handshake_task: shutdown")
                self.harvester_handshake_task = None
                return

            if peer not in self.server.get_connections():
                log.debug("handshake_task: disconnected")
                self.harvester_handshake_task = None
                return

            # Sends a handshake to the harvester
            handshake = harvester_protocol.HarvesterHandshake(
                self.get_public_keys(),
                self.pool_public_keys,
            )
            msg = make_msg(ProtocolMessageTypes.harvester_handshake, handshake)
            await peer.send_message(msg)
            self.harvester_handshake_task = None

        if peer.connection_type is NodeType.HARVESTER:
            self.plot_sync_receivers[peer.peer_node_id] = Receiver(peer, self.plot_sync_callback)
            self.harvester_handshake_task = asyncio.create_task(handshake_task())

    def set_server(self, server):
        self.server = server

    def state_changed(self, change: str, data: Dict[str, Any]):
        if self.state_changed_callback is not None:
            self.state_changed_callback(change, data)

    def handle_failed_pool_response(self, p2_singleton_puzzle_hash: bytes32, error_message: str):
        self.log.error(error_message)
        self.pool_state[p2_singleton_puzzle_hash]["pool_errors_24h"].append(
            ErrorResponse(uint16(PoolErrorCode.REQUEST_FAILED.value), error_message).to_json_dict()
        )

    def on_disconnect(self, connection: ws.WSChinillaConnection):
        self.log.info(f"peer disconnected {connection.get_peer_logging()}")
        self.state_changed("close_connection", {})
        if connection.connection_type is NodeType.HARVESTER:
            del self.plot_sync_receivers[connection.peer_node_id]
            self.state_changed("harvester_removed", {"node_id": connection.peer_node_id})

    async def plot_sync_callback(self, peer_id: bytes32, delta: Optional[Delta]) -> None:
        log.debug(f"plot_sync_callback: peer_id {peer_id}, delta {delta}")
        receiver: Receiver = self.plot_sync_receivers[peer_id]
        harvester_updated: bool = delta is not None and not delta.empty()
        if receiver.initial_sync() or harvester_updated:
            self.state_changed("harvester_update", receiver.to_dict(True))

    async def _pool_get_pool_info(self, pool_config: PoolWalletConfig) -> Optional[Dict]:
        try:
            async with aiohttp.ClientSession(trust_env=True) as session:
                async with session.get(
                    f"{pool_config.pool_url}/pool_info", ssl=ssl_context_for_root(get_mozilla_ca_crt(), log=self.log)
                ) as resp:
                    if resp.ok:
                        response: Dict = json.loads(await resp.text())
                        self.log.info(f"GET /pool_info response: {response}")
                        return response
                    else:
                        self.handle_failed_pool_response(
                            pool_config.p2_singleton_puzzle_hash,
                            f"Error in GET /pool_info {pool_config.pool_url}, {resp.status}",
                        )

        except Exception as e:
            self.handle_failed_pool_response(
                pool_config.p2_singleton_puzzle_hash, f"Exception in GET /pool_info {pool_config.pool_url}, {e}"
            )

        return None

    async def _pool_get_farmer(
        self, pool_config: PoolWalletConfig, authentication_token_timeout: uint8, authentication_sk: PrivateKey
    ) -> Optional[Dict]:
        authentication_token = get_current_authentication_token(authentication_token_timeout)
        message: bytes32 = std_hash(
            AuthenticationPayload(
                "get_farmer", pool_config.launcher_id, pool_config.target_puzzle_hash, authentication_token
            )
        )
        signature: G2Element = AugSchemeMPL.sign(authentication_sk, message)
        get_farmer_params = {
            "launcher_id": pool_config.launcher_id.hex(),
            "authentication_token": authentication_token,
            "signature": bytes(signature).hex(),
        }
        try:
            async with aiohttp.ClientSession(trust_env=True) as session:
                async with session.get(
                    f"{pool_config.pool_url}/farmer",
                    params=get_farmer_params,
                    ssl=ssl_context_for_root(get_mozilla_ca_crt(), log=self.log),
                ) as resp:
                    if resp.ok:
                        response: Dict = json.loads(await resp.text())
                        log_level = logging.INFO
                        if "error_code" in response:
                            log_level = logging.WARNING
                            self.pool_state[pool_config.p2_singleton_puzzle_hash]["pool_errors_24h"].append(response)
                        self.log.log(log_level, f"GET /farmer response: {response}")
                        return response
                    else:
                        self.handle_failed_pool_response(
                            pool_config.p2_singleton_puzzle_hash,
                            f"Error in GET /farmer {pool_config.pool_url}, {resp.status}",
                        )
        except Exception as e:
            self.handle_failed_pool_response(
                pool_config.p2_singleton_puzzle_hash, f"Exception in GET /farmer {pool_config.pool_url}, {e}"
            )
        return None

    async def _pool_post_farmer(
        self, pool_config: PoolWalletConfig, authentication_token_timeout: uint8, owner_sk: PrivateKey
    ) -> Optional[Dict]:
        auth_sk: Optional[PrivateKey] = self.get_authentication_sk(pool_config)
        assert auth_sk is not None
        post_farmer_payload: PostFarmerPayload = PostFarmerPayload(
            pool_config.launcher_id,
            get_current_authentication_token(authentication_token_timeout),
            auth_sk.get_g1(),
            pool_config.payout_instructions,
            None,
        )
        assert owner_sk.get_g1() == pool_config.owner_public_key
        signature: G2Element = AugSchemeMPL.sign(owner_sk, post_farmer_payload.get_hash())
        post_farmer_request = PostFarmerRequest(post_farmer_payload, signature)
        self.log.debug(f"POST /farmer request {post_farmer_request}")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{pool_config.pool_url}/farmer",
                    json=post_farmer_request.to_json_dict(),
                    ssl=ssl_context_for_root(get_mozilla_ca_crt(), log=self.log),
                ) as resp:
                    if resp.ok:
                        response: Dict = json.loads(await resp.text())
                        log_level = logging.INFO
                        if "error_code" in response:
                            log_level = logging.WARNING
                            self.pool_state[pool_config.p2_singleton_puzzle_hash]["pool_errors_24h"].append(response)
                        self.log.log(log_level, f"POST /farmer response: {response}")
                        return response
                    else:
                        self.handle_failed_pool_response(
                            pool_config.p2_singleton_puzzle_hash,
                            f"Error in POST /farmer {pool_config.pool_url}, {resp.status}",
                        )
        except Exception as e:
            self.handle_failed_pool_response(
                pool_config.p2_singleton_puzzle_hash, f"Exception in POST /farmer {pool_config.pool_url}, {e}"
            )
        return None

    async def _pool_put_farmer(
        self, pool_config: PoolWalletConfig, authentication_token_timeout: uint8, owner_sk: PrivateKey
    ) -> None:
        auth_sk: Optional[PrivateKey] = self.get_authentication_sk(pool_config)
        assert auth_sk is not None
        put_farmer_payload: PutFarmerPayload = PutFarmerPayload(
            pool_config.launcher_id,
            get_current_authentication_token(authentication_token_timeout),
            auth_sk.get_g1(),
            pool_config.payout_instructions,
            None,
        )
        assert owner_sk.get_g1() == pool_config.owner_public_key
        signature: G2Element = AugSchemeMPL.sign(owner_sk, put_farmer_payload.get_hash())
        put_farmer_request = PutFarmerRequest(put_farmer_payload, signature)
        self.log.debug(f"PUT /farmer request {put_farmer_request}")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.put(
                    f"{pool_config.pool_url}/farmer",
                    json=put_farmer_request.to_json_dict(),
                    ssl=ssl_context_for_root(get_mozilla_ca_crt(), log=self.log),
                ) as resp:
                    if resp.ok:
                        response: Dict = json.loads(await resp.text())
                        log_level = logging.INFO
                        if "error_code" in response:
                            log_level = logging.WARNING
                            self.pool_state[pool_config.p2_singleton_puzzle_hash]["pool_errors_24h"].append(response)
                        self.log.log(log_level, f"PUT /farmer response: {response}")
                    else:
                        self.handle_failed_pool_response(
                            pool_config.p2_singleton_puzzle_hash,
                            f"Error in PUT /farmer {pool_config.pool_url}, {resp.status}",
                        )
        except Exception as e:
            self.handle_failed_pool_response(
                pool_config.p2_singleton_puzzle_hash, f"Exception in PUT /farmer {pool_config.pool_url}, {e}"
            )

    def get_authentication_sk(self, pool_config: PoolWalletConfig) -> Optional[PrivateKey]:
        if pool_config.p2_singleton_puzzle_hash in self.authentication_keys:
            return self.authentication_keys[pool_config.p2_singleton_puzzle_hash]
        auth_sk: Optional[PrivateKey] = find_authentication_sk(self.all_root_sks, pool_config.owner_public_key)
        if auth_sk is not None:
            self.authentication_keys[pool_config.p2_singleton_puzzle_hash] = auth_sk
        return auth_sk

    async def update_pool_state(self):
        config = load_config(self._root_path, "config.yaml")

        pool_config_list: List[PoolWalletConfig] = load_pool_config(self._root_path)
        for pool_config in pool_config_list:
            p2_singleton_puzzle_hash = pool_config.p2_singleton_puzzle_hash

            try:
                authentication_sk: Optional[PrivateKey] = self.get_authentication_sk(pool_config)

                if authentication_sk is None:
                    self.log.error(f"Could not find authentication sk for {p2_singleton_puzzle_hash}")
                    continue

                add_auth_key(self._root_path, pool_config, authentication_sk.get_g1())

                if p2_singleton_puzzle_hash not in self.pool_state:
                    self.pool_state[p2_singleton_puzzle_hash] = {
                        "points_found_since_start": 0,
                        "points_found_24h": [],
                        "points_acknowledged_since_start": 0,
                        "points_acknowledged_24h": [],
                        "next_farmer_update": 0,
                        "next_pool_info_update": 0,
                        "current_points": 0,
                        "current_difficulty": None,
                        "pool_errors_24h": [],
                        "authentication_token_timeout": None,
                    }
                    self.log.info(f"Added pool: {pool_config}")
                pool_state = self.pool_state[p2_singleton_puzzle_hash]
                pool_state["pool_config"] = pool_config

                # Skip state update when self pooling
                if pool_config.pool_url == "":
                    continue

                enforce_https = config["full_node"]["selected_network"] == "vanillanet"
                if enforce_https and not pool_config.pool_url.startswith("https://"):
                    self.log.error(f"Pool URLs must be HTTPS on vanillanet {pool_config.pool_url}")
                    continue

                # TODO: Improve error handling below, inform about unexpected failures
                if time.time() >= pool_state["next_pool_info_update"]:
                    pool_state["next_pool_info_update"] = time.time() + UPDATE_POOL_INFO_INTERVAL
                    # Makes a GET request to the pool to get the updated information
                    pool_info = await self._pool_get_pool_info(pool_config)
                    if pool_info is not None and "error_code" not in pool_info:
                        pool_state["authentication_token_timeout"] = pool_info["authentication_token_timeout"]
                        # Only update the first time from GET /pool_info, gets updated from GET /farmer later
                        if pool_state["current_difficulty"] is None:
                            pool_state["current_difficulty"] = pool_info["minimum_difficulty"]

                if time.time() >= pool_state["next_farmer_update"]:
                    pool_state["next_farmer_update"] = time.time() + UPDATE_POOL_FARMER_INFO_INTERVAL
                    authentication_token_timeout = pool_state["authentication_token_timeout"]

                    async def update_pool_farmer_info() -> Tuple[Optional[GetFarmerResponse], Optional[PoolErrorCode]]:
                        # Run a GET /farmer to see if the farmer is already known by the pool
                        response = await self._pool_get_farmer(
                            pool_config, authentication_token_timeout, authentication_sk
                        )
                        farmer_response: Optional[GetFarmerResponse] = None
                        error_code_response: Optional[PoolErrorCode] = None
                        if response is not None:
                            if "error_code" not in response:
                                farmer_response = GetFarmerResponse.from_json_dict(response)
                                if farmer_response is not None:
                                    pool_state["current_difficulty"] = farmer_response.current_difficulty
                                    pool_state["current_points"] = farmer_response.current_points
                            else:
                                try:
                                    error_code_response = PoolErrorCode(response["error_code"])
                                except ValueError:
                                    self.log.error(
                                        f"Invalid error code received from the pool: {response['error_code']}"
                                    )

                        return farmer_response, error_code_response

                    if authentication_token_timeout is not None:
                        farmer_info, error_code = await update_pool_farmer_info()
                        if error_code == PoolErrorCode.FARMER_NOT_KNOWN:
                            # Make the farmer known on the pool with a POST /farmer
                            owner_sk_and_index: Optional[PrivateKey, uint32] = find_owner_sk(
                                self.all_root_sks, pool_config.owner_public_key
                            )
                            assert owner_sk_and_index is not None
                            post_response = await self._pool_post_farmer(
                                pool_config, authentication_token_timeout, owner_sk_and_index[0]
                            )
                            if post_response is not None and "error_code" not in post_response:
                                self.log.info(
                                    f"Welcome message from {pool_config.pool_url}: "
                                    f"{post_response['welcome_message']}"
                                )
                                # Now we should be able to update the local farmer info
                                farmer_info, farmer_is_known = await update_pool_farmer_info()
                                if farmer_info is None and not farmer_is_known:
                                    self.log.error("Failed to update farmer info after POST /farmer.")

                        # Update the farmer information on the pool if the payout instructions changed or if the
                        # signature is invalid (latter to make sure the pool has the correct authentication public key).
                        payout_instructions_update_required: bool = (
                            farmer_info is not None
                            and pool_config.payout_instructions.lower() != farmer_info.payout_instructions.lower()
                        )
                        if payout_instructions_update_required or error_code == PoolErrorCode.INVALID_SIGNATURE:
                            owner_sk_and_index: Optional[PrivateKey, uint32] = find_owner_sk(
                                self.all_root_sks, pool_config.owner_public_key
                            )
                            assert owner_sk_and_index is not None
                            await self._pool_put_farmer(
                                pool_config, authentication_token_timeout, owner_sk_and_index[0]
                            )
                    else:
                        self.log.warning(
                            f"No pool specific authentication_token_timeout has been set for {p2_singleton_puzzle_hash}"
                            f", check communication with the pool."
                        )

            except Exception as e:
                tb = traceback.format_exc()
                self.log.error(f"Exception in update_pool_state for {pool_config.pool_url}, {e} {tb}")

    def get_public_keys(self):
        return [child_sk.get_g1() for child_sk in self._private_keys]

    def get_private_keys(self):
        return self._private_keys

    async def get_reward_targets(self, search_for_private_key: bool) -> Dict:
        if search_for_private_key:
            all_sks = await self.get_all_private_keys()
            stop_searching_for_farmer, stop_searching_for_pool = False, False
            for i in range(500):
                if stop_searching_for_farmer and stop_searching_for_pool and i > 0:
                    break
                for sk, _ in all_sks:
                    ph = create_puzzlehash_for_pk(master_sk_to_wallet_sk(sk, uint32(i)).get_g1())

                    if ph == self.farmer_target:
                        stop_searching_for_farmer = True
                    if ph == self.pool_target:
                        stop_searching_for_pool = True
            return {
                "farmer_target": self.farmer_target_encoded,
                "pool_target": self.pool_target_encoded,
                "have_farmer_sk": stop_searching_for_farmer,
                "have_pool_sk": stop_searching_for_pool,
            }
        return {
            "farmer_target": self.farmer_target_encoded,
            "pool_target": self.pool_target_encoded,
        }

    def set_reward_targets(self, farmer_target_encoded: Optional[str], pool_target_encoded: Optional[str]):
        with lock_and_load_config(self._root_path, "config.yaml") as config:
            if farmer_target_encoded is not None:
                self.farmer_target_encoded = farmer_target_encoded
                self.farmer_target = decode_puzzle_hash(farmer_target_encoded)
                config["farmer"]["hcx_target_address"] = farmer_target_encoded
            if pool_target_encoded is not None:
                self.pool_target_encoded = pool_target_encoded
                self.pool_target = decode_puzzle_hash(pool_target_encoded)
                config["pool"]["hcx_target_address"] = pool_target_encoded
            save_config(self._root_path, "config.yaml", config)

    async def set_payout_instructions(self, launcher_id: bytes32, payout_instructions: str):
        for p2_singleton_puzzle_hash, pool_state_dict in self.pool_state.items():
            if launcher_id == pool_state_dict["pool_config"].launcher_id:
                with lock_and_load_config(self._root_path, "config.yaml") as config:
                    new_list = []
                    pool_list = config["pool"].get("pool_list", [])
                    if pool_list is not None:
                        for list_element in pool_list:
                            if hexstr_to_bytes(list_element["launcher_id"]) == bytes(launcher_id):
                                list_element["payout_instructions"] = payout_instructions
                            new_list.append(list_element)

                    config["pool"]["pool_list"] = new_list
                    save_config(self._root_path, "config.yaml", config)
                # Force a GET /farmer which triggers the PUT /farmer if it detects the changed instructions
                pool_state_dict["next_farmer_update"] = 0
                return

        self.log.warning(f"Launcher id: {launcher_id} not found")

    async def generate_login_link(self, launcher_id: bytes32) -> Optional[str]:
        for pool_state in self.pool_state.values():
            pool_config: PoolWalletConfig = pool_state["pool_config"]
            if pool_config.launcher_id == launcher_id:

                authentication_sk: Optional[PrivateKey] = self.get_authentication_sk(pool_config)
                if authentication_sk is None:
                    self.log.error(f"Could not find authentication sk for {pool_config.p2_singleton_puzzle_hash}")
                    continue
                authentication_token_timeout = pool_state["authentication_token_timeout"]
                authentication_token = get_current_authentication_token(authentication_token_timeout)
                message: bytes32 = std_hash(
                    AuthenticationPayload(
                        "get_login", pool_config.launcher_id, pool_config.target_puzzle_hash, authentication_token
                    )
                )
                signature: G2Element = AugSchemeMPL.sign(authentication_sk, message)
                return (
                    pool_config.pool_url
                    + f"/login?launcher_id={launcher_id.hex()}&authentication_token={authentication_token}"
                    f"&signature={bytes(signature).hex()}"
                )

        return None

    async def get_harvesters(self, counts_only: bool = False) -> Dict:
        harvesters: List = []
        for connection in self.server.get_connections(NodeType.HARVESTER):
            self.log.debug(f"get_harvesters host: {connection.peer_host}, node_id: {connection.peer_node_id}")
            receiver = self.plot_sync_receivers.get(connection.peer_node_id)
            if receiver is not None:
                harvesters.append(receiver.to_dict(counts_only))
            else:
                self.log.debug(
                    f"get_harvesters invalid peer: {connection.peer_host}, node_id: {connection.peer_node_id}"
                )

        return {"harvesters": harvesters}

    def get_receiver(self, node_id: bytes32) -> Receiver:
        receiver: Optional[Receiver] = self.plot_sync_receivers.get(node_id)
        if receiver is None:
            raise KeyError(f"Receiver missing for {node_id}")
        return receiver

    async def _periodically_update_pool_state_task(self):
        time_slept: uint64 = uint64(0)
        config_path: Path = config_path_for_filename(self._root_path, "config.yaml")
        while not self._shut_down:
            # Every time the config file changes, read it to check the pool state
            stat_info = config_path.stat()
            if stat_info.st_mtime > self.last_config_access_time:
                # If we detect the config file changed, refresh private keys first just in case
                self.all_root_sks: List[PrivateKey] = [sk for sk, _ in await self.get_all_private_keys()]
                self.last_config_access_time = stat_info.st_mtime
                await self.update_pool_state()
                time_slept = uint64(0)
            elif time_slept > 60:
                await self.update_pool_state()
                time_slept = uint64(0)
            time_slept += 1
            await asyncio.sleep(1)

    async def _periodically_clear_cache_and_refresh_task(self):
        time_slept: uint64 = uint64(0)
        refresh_slept = 0
        while not self._shut_down:
            try:
                if time_slept > self.constants.SUB_SLOT_TIME_TARGET:
                    now = time.time()
                    removed_keys: List[bytes32] = []
                    for key, add_time in self.cache_add_time.items():
                        if now - float(add_time) > self.constants.SUB_SLOT_TIME_TARGET * 3:
                            self.sps.pop(key, None)
                            self.proofs_of_space.pop(key, None)
                            self.quality_str_to_identifiers.pop(key, None)
                            self.number_of_responses.pop(key, None)
                            removed_keys.append(key)
                    for key in removed_keys:
                        self.cache_add_time.pop(key, None)
                    time_slept = uint64(0)
                    log.debug(
                        f"Cleared farmer cache. Num sps: {len(self.sps)} {len(self.proofs_of_space)} "
                        f"{len(self.quality_str_to_identifiers)} {len(self.number_of_responses)}"
                    )
                time_slept += 1
                refresh_slept += 1
                # Periodically refresh GUI to show the correct download/upload rate.
                if refresh_slept >= 30:
                    self.state_changed("add_connection", {})
                    refresh_slept = 0

            except Exception:
                log.error(f"_periodically_clear_cache_and_refresh_task failed: {traceback.format_exc()}")

            await asyncio.sleep(1)
