"""
http://adventofcode.com/2017/day/6
"""
from typing import List

import itertools

def count_redistribution_cycles(bank: List[int]) -> int:
    bank_memory = []
    bank_memory.append(tuple(bank))

    for i in itertools.count(1):
        bank = redistribute_blocks(bank)
        if tuple(bank) in bank_memory:
            return i
        bank_memory.append(tuple(bank))

    return 0

def redistribute_blocks(bank: List[int]) -> List[int]:
    bank_size = len(bank)
    idx = bank.index(max(bank))
    blocks = bank[idx]
    bank[idx] = 0

    while blocks > 0:
        idx += 1
        bank[idx % bank_size] += 1
        blocks -= 1

    return bank

def count_redistribution_cycles_since_last(bank: List[int]) -> int:
    bank_memory = []
    bank_memory.append(tuple(bank))

    for idx in itertools.count(1):
        bank = redistribute_blocks(bank)
        if tuple(bank) in bank_memory:
            id_last = bank_memory.index(tuple(bank))
            return idx - id_last
        bank_memory.append(tuple(bank))

    return 0


TEST_BANK = [0, 2, 7, 0]
assert count_redistribution_cycles(TEST_BANK) == 5
assert count_redistribution_cycles(TEST_BANK) == 4


if __name__ == '__main__':
    with open('day06_input.txt', 'r') as f:
        BANK = [int(x) for x in f.read().strip().split()]
    print("Number of redistribution cycles:",
          count_redistribution_cycles(BANK))
    print("Number of redistribution cycles since last:",
          count_redistribution_cycles_since_last(BANK))
