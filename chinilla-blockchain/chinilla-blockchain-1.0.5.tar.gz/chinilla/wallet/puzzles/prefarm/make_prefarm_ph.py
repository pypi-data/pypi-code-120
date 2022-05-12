from clvm.casts import int_from_bytes
from clvm_tools import binutils

from chinilla.consensus.block_rewards import calculate_base_farmer_reward, calculate_pool_reward
from chinilla.types.blockchain_format.program import Program
from chinilla.types.condition_opcodes import ConditionOpcode
from chinilla.util.bech32m import decode_puzzle_hash, encode_puzzle_hash
from chinilla.util.condition_tools import parse_sexp_to_conditions
from chinilla.util.ints import uint32
from chinilla.types.blockchain_format.sized_bytes import bytes32

address1 = "thcx15gx26ndmacfaqlq8m0yajeggzceu7cvmaz4df0hahkukes695rss6lej7h"  # Gene wallet (m/12381/8444/2/42):
address2 = "thcx1c2cguswhvmdyz9hr3q6hak2h6p9dw4rz82g4707k2xy2sarv705qcce4pn"  # Mariano address (m/12381/8444/2/0)

ph1 = decode_puzzle_hash(address1)
ph2 = decode_puzzle_hash(address2)

pool_amounts = int(calculate_pool_reward(uint32(0)) / 2)
farmer_amounts = int(calculate_base_farmer_reward(uint32(0)) / 2)

assert pool_amounts * 2 == calculate_pool_reward(uint32(0))
assert farmer_amounts * 2 == calculate_base_farmer_reward(uint32(0))


def make_puzzle(amount: int) -> int:
    puzzle = f"(q . ((51 0x{ph1.hex()} {amount}) (51 0x{ph2.hex()} {amount})))"
    # print(puzzle)

    # TODO: properly type hint clvm_tools
    assembled_puzzle = binutils.assemble(puzzle)  # type: ignore[no-untyped-call]
    puzzle_prog = Program.to(assembled_puzzle)
    print("Program: ", puzzle_prog)
    puzzle_hash = puzzle_prog.get_tree_hash()

    solution = "()"
    prefix = "hcx"
    print("PH", puzzle_hash)
    print(f"Address: {encode_puzzle_hash(puzzle_hash, prefix)}")

    result = puzzle_prog.run(solution)
    error, result_human = parse_sexp_to_conditions(result)

    total_chinilla = 0
    if error:
        print(f"Error: {error}")
    else:
        assert result_human is not None
        for cvp in result_human:
            assert len(cvp.vars) == 2
            total_chinilla += int_from_bytes(cvp.vars[1])
            print(
                f"{ConditionOpcode(cvp.opcode).name}: {encode_puzzle_hash(bytes32(cvp.vars[0]), prefix)},"
                f" amount: {int_from_bytes(cvp.vars[1])}"
            )
    return total_chinilla


total_chinilla = 0
print("Pool address: ")
total_chinilla += make_puzzle(pool_amounts)
print("\nFarmer address: ")
total_chinilla += make_puzzle(farmer_amounts)

assert total_chinilla == calculate_base_farmer_reward(uint32(0)) + calculate_pool_reward(uint32(0))
