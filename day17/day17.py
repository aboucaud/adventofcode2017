"""
http://adventofcode.com/2017/day/17
"""
from typing import List


def spinlock(steps: int, max_val: int) -> List[int]:
    buff = [0]
    idx = 0
    for i in range(max_val):
        val = i + 1
        idx = (idx + steps) % val + 1
        buff.insert(idx, val)
    return buff


def next_to_2017(steps: int) -> int:
    buff = spinlock(steps, 2017)
    return buff[buff.index(2017) + 1]


def after_zero(steps: int) -> int:
    """
    Quite fast using pypy3 < 1 sec
    """
    idx = 0
    for i in range(50000000):
        val = i + 1
        idx = (idx + steps) % val + 1
        if idx == 1:
            final_val = val
    return final_val


assert spinlock(3, 1) == [0, 1]
assert spinlock(3, 2) == [0, 2, 1]
assert spinlock(3, 3) == [0, 2, 3, 1]
assert spinlock(3, 4) == [0, 2, 4, 3, 1]
assert next_to_2017(3) == 638


with open('day17_input.txt', 'r') as f:
    INPUT = int(f.read().strip())
    print(next_to_2017(INPUT))
    print(after_zero(INPUT))
