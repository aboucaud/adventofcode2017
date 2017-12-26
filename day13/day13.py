"""
http://adventofcode.com/2017/day/13
"""
from typing import List, Dict


def parse_input(input: List[str]) -> Dict[int, int]:
    lines = [line.split(': ') for line in input]
    return {int(depth): int(range_) for depth, range_ in lines}


def scanner_at_zero(depth: int, range_: int) -> bool:
    return depth % ((range_ - 1) * 2) == 0


def severity_of(input: List[str]) -> int:
    layers = parse_input(input)
    severity = 0

    for depth, range_ in layers.items():
        if scanner_at_zero(depth, range_):
            severity += depth * range_

    return severity

# Part 2
# ------


def was_caught(layers: Dict[int, int], wait: int) -> bool:
    for depth, range_ in layers.items():
        if scanner_at_zero(depth + wait, range_):
            return True

    return False


def min_delay(input: List[str]) -> int:
    layers = parse_input(input)

    wait = 0
    while was_caught(layers, wait):
        wait += 1

    return wait


TEST = """0: 3
1: 2
4: 4
6: 4""".split('\n')

assert severity_of(TEST) == 24
assert min_delay(TEST) == 10


if __name__ == '__main__':
    with open('day13_input.txt', 'r') as f:
        lines = f.read().splitlines()
    print("Severity:", severity_of(lines))
    print("Min delay:", min_delay(lines))
