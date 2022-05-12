import os
import pickle
from pathlib import Path
from typing import List, Optional

import aiosqlite
import tempfile

from chinilla.consensus.blockchain import Blockchain
from chinilla.consensus.constants import ConsensusConstants
from chinilla.full_node.block_store import BlockStore
from chinilla.full_node.coin_store import CoinStore
from chinilla.full_node.hint_store import HintStore
from chinilla.types.full_block import FullBlock
from chinilla.util.db_wrapper import DBWrapper2
from chinilla.util.default_root import DEFAULT_ROOT_PATH
from chinilla.util.path import mkdir
from tests.block_tools import BlockTools


async def create_blockchain(constants: ConsensusConstants, db_version: int):
    db_path = Path(tempfile.NamedTemporaryFile().name)

    if db_path.exists():
        db_path.unlink()
    connection = await aiosqlite.connect(db_path)
    wrapper = DBWrapper2(connection, db_version)
    await wrapper.add_connection(await aiosqlite.connect(db_path))

    coin_store = await CoinStore.create(wrapper)
    store = await BlockStore.create(wrapper)
    hint_store = await HintStore.create(wrapper)
    bc1 = await Blockchain.create(coin_store, store, constants, hint_store, Path("."), 2)
    assert bc1.get_peak() is None
    return bc1, wrapper, db_path


def persistent_blocks(
    num_of_blocks: int,
    db_name: str,
    bt: BlockTools,
    seed: bytes = b"",
    empty_sub_slots=0,
    normalized_to_identity_cc_eos: bool = False,
    normalized_to_identity_icc_eos: bool = False,
    normalized_to_identity_cc_sp: bool = False,
    normalized_to_identity_cc_ip: bool = False,
    block_list_input: List[FullBlock] = None,
    time_per_block: Optional[float] = None,
):
    # try loading from disc, if not create new blocks.db file
    # TODO hash fixtures.py and blocktool.py, add to path, delete if the files changed
    if block_list_input is None:
        block_list_input = []
    block_path_dir = DEFAULT_ROOT_PATH.parent.joinpath("blocks")
    file_path = block_path_dir.joinpath(db_name)

    ci = os.environ.get("CI")
    if ci is not None and not file_path.exists():
        raise Exception(f"Running in CI and expected path not found: {file_path!r}")

    mkdir(block_path_dir)

    if file_path.exists():
        print(f"File found at: {file_path}")
        try:
            bytes_list = file_path.read_bytes()
            block_bytes_list: List[bytes] = pickle.loads(bytes_list)
            blocks: List[FullBlock] = []
            for block_bytes in block_bytes_list:
                blocks.append(FullBlock.from_bytes(block_bytes))
            if len(blocks) == num_of_blocks + len(block_list_input):
                print(f"\n loaded {file_path} with {len(blocks)} blocks")
                return blocks
        except EOFError:
            print("\n error reading db file")
    else:
        print(f"File not found at: {file_path}")

    print("Creating a new test db")
    return new_test_db(
        file_path,
        num_of_blocks,
        seed,
        empty_sub_slots,
        bt,
        block_list_input,
        time_per_block,
        normalized_to_identity_cc_eos,
        normalized_to_identity_icc_eos,
        normalized_to_identity_cc_sp,
        normalized_to_identity_cc_ip,
    )


def new_test_db(
    path: Path,
    num_of_blocks: int,
    seed: bytes,
    empty_sub_slots: int,
    bt: BlockTools,
    block_list_input: List[FullBlock],
    time_per_block: Optional[float],
    normalized_to_identity_cc_eos: bool = False,  # CC_EOS,
    normalized_to_identity_icc_eos: bool = False,  # ICC_EOS
    normalized_to_identity_cc_sp: bool = False,  # CC_SP,
    normalized_to_identity_cc_ip: bool = False,  # CC_IP
):
    print(f"create {path} with {num_of_blocks} blocks with ")
    blocks: List[FullBlock] = bt.get_consecutive_blocks(
        num_of_blocks,
        block_list_input=block_list_input,
        time_per_block=time_per_block,
        seed=seed,
        skip_slots=empty_sub_slots,
        normalized_to_identity_cc_eos=normalized_to_identity_cc_eos,
        normalized_to_identity_icc_eos=normalized_to_identity_icc_eos,
        normalized_to_identity_cc_sp=normalized_to_identity_cc_sp,
        normalized_to_identity_cc_ip=normalized_to_identity_cc_ip,
    )
    block_bytes_list: List[bytes] = []
    for block in blocks:
        block_bytes_list.append(bytes(block))
    bytes_fn = pickle.dumps(block_bytes_list)
    path.write_bytes(bytes_fn)
    return blocks
