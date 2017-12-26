"""
http://adventofcode.com/2017/day/5
"""
from typing import List

import itertools


def parse_input(text: str) -> List[int]:
    return [int(number) for number in text.splitlines()]


def number_of_steps(jump_list: List[int]) -> int:
    idx = 0
    for i in itertools.count(1):
        jump = jump_list[idx]
        jump_list[idx] += 1
        idx += jump
        if idx >= len(jump_list):
            return i

    return 0


def number_of_steps_v2(jump_list: List[int]) -> int:
    idx = 0
    for i in itertools.count(1):
        jump = jump_list[idx]
        if jump >= 3:
            jump_list[idx] -= 1
        else:
            jump_list[idx] += 1
        idx += jump
        if idx >= len(jump_list):
            return i

    return 0


EXAMPLE_MAZE = [0, 3, 0, 1, -3]
assert number_of_steps(EXAMPLE_MAZE[:]) == 5
assert number_of_steps_v2(EXAMPLE_MAZE[:]) == 10


if __name__ == '__main__':
    with open('day05_input.txt', 'r') as f:
        JUMPS = parse_input(f.read().strip())
    print("Number of steps:", number_of_steps(JUMPS[:]))
    print("Number of steps v2:", number_of_steps_v2(JUMPS[:]))
