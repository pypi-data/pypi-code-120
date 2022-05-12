from typing import Callable, Optional

from blspy import G1Element, G2Element
from chia_rs import serialized_length

from chinilla.types.blockchain_format.program import SerializedProgram


def skip_list(buf: memoryview, skip_item: Callable[[memoryview], memoryview]) -> memoryview:
    n = int.from_bytes(buf[:4], "big", signed=False)
    buf = buf[4:]
    for i in range(n):
        buf = skip_item(buf)
    return buf


def skip_bytes(buf: memoryview) -> memoryview:
    n = int.from_bytes(buf[:4], "big", signed=False)
    buf = buf[4:]
    assert n >= 0
    return buf[n:]


def skip_optional(buf: memoryview, skip_item: Callable[[memoryview], memoryview]) -> memoryview:

    if buf[0] == 0:
        return buf[1:]
    assert buf[0] == 1
    return skip_item(buf[1:])


def skip_bytes32(buf: memoryview) -> memoryview:
    return buf[32:]


def skip_uint32(buf: memoryview) -> memoryview:
    return buf[4:]


def skip_uint64(buf: memoryview) -> memoryview:
    return buf[8:]


def skip_uint128(buf: memoryview) -> memoryview:
    return buf[16:]


def skip_uint8(buf: memoryview) -> memoryview:
    return buf[1:]


def skip_bool(buf: memoryview) -> memoryview:
    assert buf[0] in [0, 1]
    return buf[1:]


# def skip_class_group_element(buf: memoryview) -> memoryview:
#    return buf[100:]  # bytes100


def skip_vdf_info(buf: memoryview) -> memoryview:
    #    buf = skip_bytes32(buf)
    #    buf = skip_uint64(buf)
    #    return skip_class_group_element(buf)
    return buf[32 + 8 + 100 :]


def skip_vdf_proof(buf: memoryview) -> memoryview:
    buf = skip_uint8(buf)  # witness_type
    buf = skip_bytes(buf)  # witness
    return skip_bool(buf)  # normalized_to_identity


def skip_challenge_chain_sub_slot(buf: memoryview) -> memoryview:
    buf = skip_vdf_info(buf)
    buf = skip_optional(buf, skip_bytes32)  # infused challenge chain sub skit hash
    buf = skip_optional(buf, skip_bytes32)  # subepoch_summary_hash
    buf = skip_optional(buf, skip_uint64)  # new_sub_slot_iters
    return skip_optional(buf, skip_uint64)  # new_difficulty


def skip_infused_challenge_chain(buf: memoryview) -> memoryview:
    return skip_vdf_info(buf)  # infused_challenge_chain_end_of_slot_vdf


def skip_reward_chain_sub_slot(buf: memoryview) -> memoryview:
    buf = skip_vdf_info(buf)  # end_of_slot_vdf
    buf = skip_bytes32(buf)  # challenge_chain_sub_slot_hash
    buf = skip_optional(buf, skip_bytes32)  # infused_challenge_chain_sub_slot_hash
    return skip_uint8(buf)


def skip_sub_slot_proofs(buf: memoryview) -> memoryview:
    buf = skip_vdf_proof(buf)  # challenge_chain_slot_proof
    buf = skip_optional(buf, skip_vdf_proof)  # infused_challenge_chain_slot_proof
    return skip_vdf_proof(buf)  # reward_chain_slot_proof


def skip_end_of_sub_slot_bundle(buf: memoryview) -> memoryview:
    buf = skip_challenge_chain_sub_slot(buf)
    buf = skip_optional(buf, skip_infused_challenge_chain)
    buf = skip_reward_chain_sub_slot(buf)
    return skip_sub_slot_proofs(buf)


def skip_g1_element(buf: memoryview) -> memoryview:
    return buf[G1Element.SIZE :]


def skip_g2_element(buf: memoryview) -> memoryview:
    return buf[G2Element.SIZE :]


def skip_proof_of_space(buf: memoryview) -> memoryview:
    buf = skip_bytes32(buf)  # challenge
    buf = skip_optional(buf, skip_g1_element)  # pool_public_key
    buf = skip_optional(buf, skip_bytes32)  # pool_contract_puzzle_hash
    buf = skip_g1_element(buf)  # plot_public_key
    buf = skip_uint8(buf)  # size
    return skip_bytes(buf)  # proof


def skip_reward_chain_block(buf: memoryview) -> memoryview:
    buf = skip_uint128(buf)  # weight
    buf = skip_uint32(buf)  # height
    buf = skip_uint128(buf)  # total_iters
    buf = skip_uint8(buf)  # signage_point_index
    buf = skip_bytes32(buf)  # pos_ss_cc_challenge_hash

    buf = skip_proof_of_space(buf)  # proof_of_space
    buf = skip_optional(buf, skip_vdf_info)  # challenge_chain_sp_vdf
    buf = skip_g2_element(buf)  # challenge_chain_sp_signature
    buf = skip_vdf_info(buf)  # challenge_chain_ip_vdf
    buf = skip_optional(buf, skip_vdf_info)  # reward_chain_sp_vdf
    buf = skip_g2_element(buf)  # reward_chain_sp_signature
    buf = skip_vdf_info(buf)  # reward_chain_ip_vdf
    buf = skip_optional(buf, skip_vdf_info)  # infused_challenge_chain_ip_vdf
    return skip_bool(buf)  # is_transaction_block


def skip_pool_target(buf: memoryview) -> memoryview:
    # buf = skip_bytes32(buf)  # puzzle_hash
    # return skip_uint32(buf)  # max_height
    return buf[32 + 4 :]


def skip_foliage_block_data(buf: memoryview) -> memoryview:
    buf = skip_bytes32(buf)  # unfinished_reward_block_hash
    buf = skip_pool_target(buf)  # pool_target
    buf = skip_optional(buf, skip_g2_element)  # pool_signature
    buf = skip_bytes32(buf)  # farmer_reward_puzzle_hash
    return skip_bytes32(buf)  # extension_data


def skip_foliage(buf: memoryview) -> memoryview:
    buf = skip_bytes32(buf)  # prev_block_hash
    buf = skip_bytes32(buf)  # reward_block_hash
    buf = skip_foliage_block_data(buf)  # foliage_block_data
    buf = skip_g2_element(buf)  # foliage_block_data_signature
    buf = skip_optional(buf, skip_bytes32)  # foliage_transaction_block_hash
    return skip_optional(buf, skip_g2_element)  # foliage_transaction_block_signature


def skip_foliage_transaction_block(buf: memoryview) -> memoryview:
    # buf = skip_bytes32(buf)  # prev_transaction_block_hash
    # buf = skip_uint64(buf)  # timestamp
    # buf = skip_bytes32(buf)  # filter_hash
    # buf = skip_bytes32(buf)  # additions_root
    # buf = skip_bytes32(buf)  # removals_root
    # return skip_bytes32(buf)  # transactions_info_hash
    return buf[32 + 8 + 32 + 32 + 32 + 32 :]


def skip_coin(buf: memoryview) -> memoryview:
    # buf = skip_bytes32(buf)  # parent_coin_info
    # buf = skip_bytes32(buf)  # puzzle_hash
    # return skip_uint64(buf)  # amount
    return buf[32 + 32 + 8 :]


def skip_transactions_info(buf: memoryview) -> memoryview:
    # buf = skip_bytes32(buf)  # generator_root
    # buf = skip_bytes32(buf)  # generator_refs_root
    # buf = skip_g2_element(buf)  # aggregated_signature
    # buf = skip_uint64(buf)  # fees
    # buf = skip_uint64(buf)  # cost
    buf = buf[32 + 32 + G2Element.SIZE + 8 + 8 :]
    return skip_list(buf, skip_coin)


def generator_from_block(buf: memoryview) -> Optional[SerializedProgram]:
    buf = skip_list(buf, skip_end_of_sub_slot_bundle)  # finished_sub_slots
    buf = skip_reward_chain_block(buf)  # reward_chain_block
    buf = skip_optional(buf, skip_vdf_proof)  # challenge_chain_sp_proof
    buf = skip_vdf_proof(buf)  # challenge_chain_ip_proof
    buf = skip_optional(buf, skip_vdf_proof)  # reward_chain_sp_proof
    buf = skip_vdf_proof(buf)  # reward_chain_ip_proof
    buf = skip_optional(buf, skip_vdf_proof)  # infused_challenge_chain_ip_proof
    buf = skip_foliage(buf)  # foliage
    buf = skip_optional(buf, skip_foliage_transaction_block)  # foliage_transaction_block
    buf = skip_optional(buf, skip_transactions_info)  # transactions_info

    # this is the transactions_generator optional
    if buf[0] == 0:
        return None

    buf = buf[1:]
    length = serialized_length(buf)
    return SerializedProgram.from_bytes(bytes(buf[:length]))
