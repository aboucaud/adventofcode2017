"""
http://adventofcode.com/2017/day/15
"""
from typing import List, Iterator

FACTOR_A = 16807
FACTOR_B = 48271
DIVIDEND = 2147483647


def matching_pairs(gen_input: List[str], size: int = 40_000_000) -> int:
    pairs = 0

    gen_a = generator(int(gen_input[0]), FACTOR_A, size)
    gen_b = generator(int(gen_input[1]), FACTOR_B, size)
    for val_a, val_b in zip(gen_a, gen_b):
        if val_a[16:] == val_b[16:]:
            pairs += 1

    return pairs


def generator(val: int, factor: int, n_iter: int) -> Iterator[str]:
    for _ in range(n_iter):
        res = (val * factor) % DIVIDEND
        val = res
        yield to_binary(res)


def to_binary(val: int) -> str:
    return bin(val)[2:].zfill(32)


def generator_multiple(val: int, factor: int, n_iter: int, multiple: int) -> Iterator[str]:
    i = 0
    while i < n_iter:
        res = (val * factor) % DIVIDEND
        val = res
        if res % multiple != 0:
            continue
        yield to_binary(res)
        i += 1


def matching_pairs_multiple(gen_input: List[str], size: int = 5_000_000) -> int:
    pairs = 0
    gen_a = generator_multiple(int(gen_input[0]), FACTOR_A, size, 4)
    gen_b = generator_multiple(int(gen_input[1]), FACTOR_B, size, 8)
    for val_a, val_b in zip(gen_a, gen_b):
        if val_a[16:] == val_b[16:]:
            pairs += 1

    return pairs


TEST = """65
8921""".splitlines()
assert matching_pairs(TEST, 5) == 1
assert matching_pairs(TEST) == 588

assert matching_pairs_multiple(TEST, 1057) == 1
assert matching_pairs_multiple(TEST) == 309


with open('day15_input.txt', 'r') as f:
    INPUT = f.read().splitlines()
print('Number of matching pairs:', matching_pairs(INPUT))
print('Number of multiple matching pairs:', matching_pairs_multiple(INPUT))

