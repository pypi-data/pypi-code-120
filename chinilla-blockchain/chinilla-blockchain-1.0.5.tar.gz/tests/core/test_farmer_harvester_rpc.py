import logging
import operator
import time
from math import ceil
from os import mkdir
from pathlib import Path
from shutil import copy
from typing import Any, Awaitable, Callable, Dict, List, Union, cast

import pytest
import pytest_asyncio

from chinilla.consensus.coinbase import create_puzzlehash_for_pk
from chinilla.plot_sync.receiver import Receiver
from chinilla.plotting.util import add_plot_directory
from chinilla.protocols import farmer_protocol
from chinilla.protocols.harvester_protocol import Plot
from chinilla.rpc.farmer_rpc_api import (
    FarmerRpcApi,
    FilterItem,
    PaginatedRequestData,
    PlotInfoRequestData,
    PlotPathRequestData,
    plot_matches_filter,
)
from chinilla.rpc.farmer_rpc_client import FarmerRpcClient
from chinilla.rpc.harvester_rpc_api import HarvesterRpcApi
from chinilla.rpc.harvester_rpc_client import HarvesterRpcClient
from chinilla.rpc.rpc_server import start_rpc_server
from chinilla.types.blockchain_format.sized_bytes import bytes32
from chinilla.util.bech32m import decode_puzzle_hash, encode_puzzle_hash
from chinilla.util.byte_types import hexstr_to_bytes
from chinilla.util.config import load_config, lock_and_load_config, save_config
from chinilla.util.hash import std_hash
from chinilla.util.ints import uint8, uint16, uint32, uint64
from chinilla.util.misc import get_list_or_len
from chinilla.util.streamable import dataclass_from_dict
from chinilla.wallet.derive_keys import master_sk_to_wallet_sk
from tests.block_tools import get_plot_dir
from tests.plot_sync.test_delta import dummy_plot
from tests.setup_nodes import setup_harvester_farmer, test_constants
from tests.time_out_assert import time_out_assert, time_out_assert_custom_interval
from tests.util.rpc import validate_get_routes
from tests.util.socket import find_available_listen_port

log = logging.getLogger(__name__)


async def wait_for_plot_sync(receiver: Receiver, previous_last_sync_id: uint64) -> None:
    def wait():
        current_last_sync_id = receiver.last_sync().sync_id
        return current_last_sync_id != 0 and current_last_sync_id != previous_last_sync_id

    await time_out_assert(30, wait)


@pytest_asyncio.fixture(scope="function")
async def harvester_farmer_simulation(bt, tmp_path):
    async for _ in setup_harvester_farmer(bt, tmp_path, test_constants, start_services=True):
        yield _


@pytest_asyncio.fixture(scope="function")
async def harvester_farmer_environment(bt, harvester_farmer_simulation, self_hostname):
    harvester_service, farmer_service = harvester_farmer_simulation

    def stop_node_cb():
        pass

    config = bt.config
    hostname = config["self_hostname"]
    daemon_port = config["daemon_port"]

    farmer_rpc_api = FarmerRpcApi(farmer_service._api.farmer)
    harvester_rpc_api = HarvesterRpcApi(harvester_service._node)

    rpc_port_farmer = uint16(find_available_listen_port("farmer rpc"))
    rpc_port_harvester = uint16(find_available_listen_port("harvester rpc"))

    rpc_cleanup = await start_rpc_server(
        farmer_rpc_api,
        hostname,
        daemon_port,
        rpc_port_farmer,
        stop_node_cb,
        bt.root_path,
        config,
        connect_to_daemon=False,
    )
    rpc_cleanup_2 = await start_rpc_server(
        harvester_rpc_api,
        hostname,
        daemon_port,
        rpc_port_harvester,
        stop_node_cb,
        bt.root_path,
        config,
        connect_to_daemon=False,
    )

    farmer_rpc_client = await FarmerRpcClient.create(self_hostname, rpc_port_farmer, bt.root_path, config)
    harvester_rpc_client = await HarvesterRpcClient.create(self_hostname, rpc_port_harvester, bt.root_path, config)

    async def have_connections():
        return len(await farmer_rpc_client.get_connections()) > 0

    await time_out_assert(15, have_connections, True)

    yield farmer_service, farmer_rpc_api, farmer_rpc_client, harvester_service, harvester_rpc_api, harvester_rpc_client

    farmer_rpc_client.close()
    harvester_rpc_client.close()
    await farmer_rpc_client.await_closed()
    await harvester_rpc_client.await_closed()
    await rpc_cleanup()
    await rpc_cleanup_2()


@pytest.mark.asyncio
async def test_get_routes(harvester_farmer_environment):
    (
        farmer_service,
        farmer_rpc_api,
        farmer_rpc_client,
        harvester_service,
        harvester_rpc_api,
        harvester_rpc_client,
    ) = harvester_farmer_environment
    await validate_get_routes(farmer_rpc_client, farmer_rpc_api)
    await validate_get_routes(harvester_rpc_client, harvester_rpc_api)


@pytest.mark.parametrize("endpoint", ["get_harvesters", "get_harvesters_summary"])
@pytest.mark.asyncio
async def test_farmer_get_harvesters_and_summary(harvester_farmer_environment, endpoint: str):
    (
        farmer_service,
        farmer_rpc_api,
        farmer_rpc_client,
        harvester_service,
        harvester_rpc_api,
        harvester_rpc_client,
    ) = harvester_farmer_environment
    harvester = harvester_service._node

    harvester_plots = []

    async def non_zero_plots() -> bool:
        res = await harvester_rpc_client.get_plots()
        nonlocal harvester_plots
        harvester_plots = res["plots"]
        return len(harvester_plots) > 0

    await time_out_assert(10, non_zero_plots)

    async def test_get_harvesters():
        nonlocal harvester_plots
        harvester.plot_manager.trigger_refresh()
        await time_out_assert(5, harvester.plot_manager.needs_refresh, value=False)
        farmer_res = await getattr(farmer_rpc_client, endpoint)()

        if len(list(farmer_res["harvesters"])) != 1:
            log.error(f"test_get_harvesters: invalid harvesters {list(farmer_res['harvesters'])}")
            return False

        if farmer_res["harvesters"][0]["last_sync_time"] is None:
            log.error(f"test_get_harvesters: sync not done {list(farmer_res['harvesters'])}")
            return False

        harvester_dict = farmer_res["harvesters"][0]
        counts_only: bool = endpoint == "get_harvesters_summary"

        if not counts_only:
            harvester_dict["plots"] = sorted(harvester_dict["plots"], key=lambda item: item["filename"])
            harvester_plots = sorted(harvester_plots, key=lambda item: item["filename"])

        assert harvester_dict["plots"] == get_list_or_len(harvester_plots, counts_only)
        assert harvester_dict["failed_to_open_filenames"] == get_list_or_len([], counts_only)
        assert harvester_dict["no_key_filenames"] == get_list_or_len([], counts_only)
        assert harvester_dict["duplicates"] == get_list_or_len([], counts_only)

        return True

    await time_out_assert_custom_interval(30, 1, test_get_harvesters)


@pytest.mark.asyncio
async def test_farmer_signage_point_endpoints(harvester_farmer_environment):
    (
        farmer_service,
        farmer_rpc_api,
        farmer_rpc_client,
        harvester_service,
        harvester_rpc_api,
        harvester_rpc_client,
    ) = harvester_farmer_environment
    farmer_api = farmer_service._api

    assert (await farmer_rpc_client.get_signage_point(std_hash(b"2"))) is None
    assert len(await farmer_rpc_client.get_signage_points()) == 0

    async def have_signage_points():
        return len(await farmer_rpc_client.get_signage_points()) > 0

    sp = farmer_protocol.NewSignagePoint(
        std_hash(b"1"), std_hash(b"2"), std_hash(b"3"), uint64(1), uint64(1000000), uint8(2)
    )
    await farmer_api.new_signage_point(sp)

    await time_out_assert(5, have_signage_points, True)
    assert (await farmer_rpc_client.get_signage_point(std_hash(b"2"))) is not None


@pytest.mark.asyncio
async def test_farmer_reward_target_endpoints(bt, harvester_farmer_environment):
    (
        farmer_service,
        farmer_rpc_api,
        farmer_rpc_client,
        harvester_service,
        harvester_rpc_api,
        harvester_rpc_client,
    ) = harvester_farmer_environment
    farmer_api = farmer_service._api

    targets_1 = await farmer_rpc_client.get_reward_targets(False)
    assert "have_pool_sk" not in targets_1
    assert "have_farmer_sk" not in targets_1
    targets_2 = await farmer_rpc_client.get_reward_targets(True)
    assert targets_2["have_pool_sk"] and targets_2["have_farmer_sk"]

    new_ph: bytes32 = create_puzzlehash_for_pk(master_sk_to_wallet_sk(bt.farmer_master_sk, uint32(10)).get_g1())
    new_ph_2: bytes32 = create_puzzlehash_for_pk(master_sk_to_wallet_sk(bt.pool_master_sk, uint32(472)).get_g1())

    await farmer_rpc_client.set_reward_targets(encode_puzzle_hash(new_ph, "hcx"), encode_puzzle_hash(new_ph_2, "hcx"))
    targets_3 = await farmer_rpc_client.get_reward_targets(True)
    assert decode_puzzle_hash(targets_3["farmer_target"]) == new_ph
    assert decode_puzzle_hash(targets_3["pool_target"]) == new_ph_2
    assert targets_3["have_pool_sk"] and targets_3["have_farmer_sk"]

    new_ph_3: bytes32 = create_puzzlehash_for_pk(master_sk_to_wallet_sk(bt.pool_master_sk, uint32(1888)).get_g1())
    await farmer_rpc_client.set_reward_targets(None, encode_puzzle_hash(new_ph_3, "hcx"))
    targets_4 = await farmer_rpc_client.get_reward_targets(True)
    assert decode_puzzle_hash(targets_4["farmer_target"]) == new_ph
    assert decode_puzzle_hash(targets_4["pool_target"]) == new_ph_3
    assert not targets_4["have_pool_sk"] and targets_3["have_farmer_sk"]

    root_path = farmer_api.farmer._root_path
    config = load_config(root_path, "config.yaml")
    assert config["farmer"]["hcx_target_address"] == encode_puzzle_hash(new_ph, "hcx")
    assert config["pool"]["hcx_target_address"] == encode_puzzle_hash(new_ph_3, "hcx")

    new_ph_3_encoded = encode_puzzle_hash(new_ph_3, "hcx")
    added_char = new_ph_3_encoded + "a"
    with pytest.raises(ValueError):
        await farmer_rpc_client.set_reward_targets(None, added_char)

    replaced_char = new_ph_3_encoded[0:-1] + "a"
    with pytest.raises(ValueError):
        await farmer_rpc_client.set_reward_targets(None, replaced_char)


@pytest.mark.asyncio
async def test_farmer_get_pool_state(harvester_farmer_environment, self_hostname):
    (
        farmer_service,
        farmer_rpc_api,
        farmer_rpc_client,
        harvester_service,
        harvester_rpc_api,
        harvester_rpc_client,
    ) = harvester_farmer_environment
    farmer_api = farmer_service._api

    assert len((await farmer_rpc_client.get_pool_state())["pool_state"]) == 0
    pool_list = [
        {
            "launcher_id": "ae4ef3b9bfe68949691281a015a9c16630fc8f66d48c19ca548fb80768791afa",
            "owner_public_key": "aa11e92274c0f6a2449fd0c7cfab4a38f943289dbe2214c808b36390c34eacfaa1d4c8f3c6ec582ac502ff32228679a0",  # noqa
            "payout_instructions": "c2b08e41d766da4116e388357ed957d04ad754623a915f3fd65188a8746cf3e8",
            "pool_url": self_hostname,
            "p2_singleton_puzzle_hash": "16e4bac26558d315cded63d4c5860e98deb447cc59146dd4de06ce7394b14f17",
            "target_puzzle_hash": "344587cf06a39db471d2cc027504e8688a0a67cce961253500c956c73603fd58",
        }
    ]

    root_path = farmer_api.farmer._root_path
    with lock_and_load_config(root_path, "config.yaml") as config:
        config["pool"]["pool_list"] = pool_list
        save_config(root_path, "config.yaml", config)
    await farmer_api.farmer.update_pool_state()

    pool_state = (await farmer_rpc_client.get_pool_state())["pool_state"]
    assert len(pool_state) == 1
    assert (
        pool_state[0]["pool_config"]["payout_instructions"]
        == "c2b08e41d766da4116e388357ed957d04ad754623a915f3fd65188a8746cf3e8"
    )
    await farmer_rpc_client.set_payout_instructions(
        hexstr_to_bytes(pool_state[0]["pool_config"]["launcher_id"]), "1234vy"
    )
    await farmer_api.farmer.update_pool_state()
    pool_state = (await farmer_rpc_client.get_pool_state())["pool_state"]
    assert pool_state[0]["pool_config"]["payout_instructions"] == "1234vy"

    now = time.time()
    # Big arbitrary numbers used to be unlikely to accidentally collide.
    before_24h = (now - (25 * 60 * 60), 29984713)
    since_24h = (now - (23 * 60 * 60), 93049817)
    for p2_singleton_puzzle_hash, pool_dict in farmer_api.farmer.pool_state.items():
        for key in ["points_found_24h", "points_acknowledged_24h"]:
            pool_dict[key].insert(0, since_24h)
            pool_dict[key].insert(0, before_24h)

    sp = farmer_protocol.NewSignagePoint(
        std_hash(b"1"), std_hash(b"2"), std_hash(b"3"), uint64(1), uint64(1000000), uint8(2)
    )
    await farmer_api.new_signage_point(sp)
    client_pool_state = await farmer_rpc_client.get_pool_state()
    for pool_dict in client_pool_state["pool_state"]:
        for key in ["points_found_24h", "points_acknowledged_24h"]:
            assert pool_dict[key][0] == list(since_24h)


@pytest.mark.asyncio
async def test_farmer_get_pool_state_plot_count(harvester_farmer_environment, self_hostname: str) -> None:
    (
        farmer_service,
        farmer_rpc_api,
        farmer_rpc_client,
        harvester_service,
        harvester_rpc_api,
        harvester_rpc_client,
    ) = harvester_farmer_environment
    farmer_api = farmer_service._api

    async def wait_for_plot_sync() -> bool:
        try:
            return (await farmer_rpc_client.get_harvesters_summary())["harvesters"][0]["plots"] > 0
        except Exception:
            return False

    await time_out_assert(15, wait_for_plot_sync, True)

    assert len((await farmer_rpc_client.get_pool_state())["pool_state"]) == 0

    pool_contract_puzzle_hash: bytes32 = bytes32.from_hexstr(
        "1b9d1eaa3c6a9b27cd90ad9070eb012794a74b277446417bc7b904145010c087"
    )
    pool_list = [
        {
            "launcher_id": "ae4ef3b9bfe68949691281a015a9c16630fc8f66d48c19ca548fb80768791afa",
            "owner_public_key": "aa11e92274c0f6a2449fd0c7cfab4a38f943289dbe2214c808b36390c34eacfaa1d4c8f3c6ec582ac502ff32228679a0",  # noqa
            "payout_instructions": "c2b08e41d766da4116e388357ed957d04ad754623a915f3fd65188a8746cf3e8",
            "pool_url": self_hostname,
            "p2_singleton_puzzle_hash": pool_contract_puzzle_hash.hex(),
            "target_puzzle_hash": "344587cf06a39db471d2cc027504e8688a0a67cce961253500c956c73603fd58",
        }
    ]

    root_path = farmer_api.farmer._root_path
    with lock_and_load_config(root_path, "config.yaml") as config:
        config["pool"]["pool_list"] = pool_list
        save_config(root_path, "config.yaml", config)
    await farmer_api.farmer.update_pool_state()

    pool_plot_count = (await farmer_rpc_client.get_pool_state())["pool_state"][0]["plot_count"]
    assert pool_plot_count == 5

    # TODO: Maybe improve this to not remove from Receiver directly but instead from the harvester and then wait for
    #       plot sync event.
    async def remove_all_and_validate() -> bool:
        nonlocal pool_plot_count
        receiver = farmer_api.farmer.plot_sync_receivers[harvester_service._server.node_id]
        for path, plot in receiver.plots().copy().items():
            if plot.pool_contract_puzzle_hash == pool_contract_puzzle_hash:
                del receiver.plots()[path]
                pool_plot_count -= 1
        plot_count = (await farmer_rpc_client.get_pool_state())["pool_state"][0]["plot_count"]
        assert plot_count == pool_plot_count
        return plot_count

    await time_out_assert(15, remove_all_and_validate, False)
    assert (await farmer_rpc_client.get_pool_state())["pool_state"][0]["plot_count"] == 0


@pytest.mark.parametrize(
    "filter_item, match",
    [
        (FilterItem("filename", "1"), True),
        (FilterItem("filename", "12"), True),
        (FilterItem("filename", "123"), True),
        (FilterItem("filename", "1234"), False),
        (FilterItem("filename", "23"), True),
        (FilterItem("filename", "3"), True),
        (FilterItem("filename", "0123"), False),
        (FilterItem("pool_contract_puzzle_hash", None), True),
        (FilterItem("pool_contract_puzzle_hash", "1"), False),
    ],
)
def test_plot_matches_filter(filter_item: FilterItem, match: bool):
    assert plot_matches_filter(dummy_plot("123"), filter_item) == match


@pytest.mark.parametrize(
    "endpoint, filtering, sort_key, reverse, expected_plot_count",
    [
        (FarmerRpcClient.get_harvester_plots_valid, [], "filename", False, 20),
        (FarmerRpcClient.get_harvester_plots_valid, [], "size", True, 20),
        (
            FarmerRpcClient.get_harvester_plots_valid,
            [FilterItem("pool_contract_puzzle_hash", None)],
            "file_size",
            True,
            15,
        ),
        (
            FarmerRpcClient.get_harvester_plots_valid,
            [FilterItem("size", "20"), FilterItem("filename", "81")],
            "plot_id",
            False,
            4,
        ),
        (FarmerRpcClient.get_harvester_plots_invalid, [], None, True, 13),
        (FarmerRpcClient.get_harvester_plots_invalid, ["invalid_0"], None, False, 6),
        (FarmerRpcClient.get_harvester_plots_invalid, ["inval", "lid_1/"], None, False, 2),
        (FarmerRpcClient.get_harvester_plots_keys_missing, [], None, True, 3),
        (FarmerRpcClient.get_harvester_plots_keys_missing, ["keys_missing_1"], None, False, 2),
        (FarmerRpcClient.get_harvester_plots_duplicates, [], None, True, 7),
        (FarmerRpcClient.get_harvester_plots_duplicates, ["duplicates_0"], None, False, 3),
    ],
)
@pytest.mark.asyncio
async def test_farmer_get_harvester_plots_endpoints(
    harvester_farmer_environment: Any,
    endpoint: Callable[[FarmerRpcClient, PaginatedRequestData], Awaitable[Dict[str, Any]]],
    filtering: Union[List[FilterItem], List[str]],
    sort_key: str,
    reverse: bool,
    expected_plot_count: int,
) -> None:
    (
        farmer_service,
        farmer_rpc_api,
        farmer_rpc_client,
        harvester_service,
        harvester_rpc_api,
        harvester_rpc_client,
    ) = harvester_farmer_environment

    harvester = harvester_service._node
    harvester_id = harvester_service._server.node_id
    receiver = farmer_service._api.farmer.plot_sync_receivers[harvester_id]

    if receiver.initial_sync():
        await wait_for_plot_sync(receiver, receiver.last_sync().sync_id)

    harvester_plots = (await harvester_rpc_client.get_plots())["plots"]
    plots = []

    request: PaginatedRequestData
    if endpoint == FarmerRpcClient.get_harvester_plots_valid:
        request = PlotInfoRequestData(harvester_id, 0, -1, cast(List[FilterItem], filtering), sort_key, reverse)
    else:
        request = PlotPathRequestData(harvester_id, 0, -1, cast(List[str], filtering), reverse)

    def add_plot_directories(prefix: str, count: int) -> List[Path]:
        new_paths = []
        for i in range(count):
            new_paths.append(harvester.root_path / f"{prefix}_{i}")
            mkdir(new_paths[-1])
            add_plot_directory(harvester.root_path, str(new_paths[-1]))
        return new_paths

    # Generate the plot data and
    if endpoint == FarmerRpcClient.get_harvester_plots_valid:
        plots = harvester_plots
    elif endpoint == FarmerRpcClient.get_harvester_plots_invalid:
        invalid_paths = add_plot_directories("invalid", 3)
        for dir_index, r in [(0, range(0, 6)), (1, range(6, 8)), (2, range(8, 13))]:
            plots += [str(invalid_paths[dir_index] / f"{i}.plot") for i in r]
        for plot in plots:
            with open(plot, "w"):
                pass
    elif endpoint == FarmerRpcClient.get_harvester_plots_keys_missing:
        keys_missing_plots = [path for path in (Path(get_plot_dir()) / "not_in_keychain").iterdir() if path.is_file()]
        keys_missing_paths = add_plot_directories("keys_missing", 2)
        for dir_index, copy_plots in [(0, keys_missing_plots[:1]), (1, keys_missing_plots[1:3])]:
            for plot in copy_plots:
                copy(plot, keys_missing_paths[dir_index])
                plots.append(str(keys_missing_paths[dir_index] / plot.name))

    elif endpoint == FarmerRpcClient.get_harvester_plots_duplicates:
        duplicate_paths = add_plot_directories("duplicates", 2)
        for dir_index, r in [(0, range(0, 3)), (1, range(3, 7))]:
            for i in r:
                plot_path = Path(harvester_plots[i]["filename"])
                plots.append(str(duplicate_paths[dir_index] / plot_path.name))
                copy(plot_path, plots[-1])

    # Sort and filter the data
    if endpoint == FarmerRpcClient.get_harvester_plots_valid:
        for filter_item in filtering:
            assert isinstance(filter_item, FilterItem)
            plots = [plot for plot in plots if plot_matches_filter(dataclass_from_dict(Plot, plot), filter_item)]
        plots.sort(key=operator.itemgetter(sort_key, "plot_id"), reverse=reverse)
    else:
        for filter_item in filtering:
            plots = [plot for plot in plots if filter_item in plot]
        plots.sort(reverse=reverse)

    total_count = len(plots)
    assert total_count == expected_plot_count

    last_sync_id = receiver.last_sync().sync_id

    harvester.plot_manager.trigger_refresh()
    harvester.plot_manager.start_refreshing()

    await wait_for_plot_sync(receiver, last_sync_id)

    for page_size in [1, int(total_count / 2), total_count - 1, total_count, total_count + 1, 100]:
        request.page_size = page_size
        expected_page_count = ceil(total_count / page_size)
        for page in range(expected_page_count):
            request.page = page
            page_result = await endpoint(farmer_rpc_client, request)
            offset = page * page_size
            expected_plots = plots[offset : offset + page_size]
            assert page_result == {
                "success": True,
                "node_id": harvester_id.hex(),
                "page": page,
                "page_count": expected_page_count,
                "total_count": total_count,
                "plots": expected_plots,
            }
