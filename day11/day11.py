"""
http://adventofcode.com/2017/day/11
"""
from typing import List


def number_of_steps_away(paths: List[str]) -> int:
    axis_ns = 0
    axis_nesw = 0
    axis_nwse = 0

    for path in paths:
        if path == 'n':
            axis_ns += 1
        if path == 's':
            axis_ns -= 1
        if path == 'ne':
            axis_nesw += 1
        if path == 'sw':
            axis_nesw -= 1
        if path == 'nw':
            axis_nwse += 1
        if path == 'se':
            axis_nwse -= 1

    if axis_nwse > 0:
        if axis_nesw > 0:
            step = min(axis_nwse, axis_nesw)
            axis_ns += step
            axis_nwse -= step
            axis_nesw -= step
        if axis_ns < 0:
            step = min(axis_nwse, -axis_ns)
            axis_ns += step
            axis_nesw -= step
            axis_nwse -= step
    if axis_nesw > 0:
        if axis_ns < 0:
            step = min(axis_nesw, -axis_ns)
            axis_ns += step
            axis_nesw -= step
            axis_nwse -= step

    if axis_nwse < 0:
        if axis_nesw < 0:
            step = min(-axis_nwse, -axis_nesw)
            axis_ns -= step
            axis_nwse += step
            axis_nesw += step
        if axis_ns > 0:
            step = min(-axis_nwse, -axis_ns)
            axis_ns -= step
            axis_nesw += step
            axis_nwse += step
    if axis_nesw < 0:
        if axis_ns > 0:
            step = min(-axis_nesw, -axis_ns)
            axis_ns -= step
            axis_nesw += step
            axis_nwse += step

    return abs(axis_ns) + abs(axis_nwse) + abs(axis_nesw)


assert number_of_steps_away(["ne", "ne", "ne"]) == 3
assert number_of_steps_away(["ne", "ne", "sw", "sw"]) == 0
assert number_of_steps_away(["ne", "ne", "s", "s"]) == 2
assert number_of_steps_away(["se", "sw", "se", "sw", "sw"]) == 3


def max_number_of_steps(paths: List[str]) -> int:
    max_steps = 0
    for idx in range(1, len(paths) + 1):
        max_steps = max(number_of_steps_away(paths[:idx]), max_steps)

    return max_steps


assert max_number_of_steps(["ne", "ne", "ne"]) == 3
assert max_number_of_steps(["ne", "ne", "sw", "sw"]) == 2
assert max_number_of_steps(["ne", "ne", "s", "s"]) == 2
assert max_number_of_steps(["se", "sw", "se", "sw", "sw"]) == 3


if __name__ == '__main__':
    with open('day11_input.txt', 'r') as f:
        steps = f.read().strip().split(',')
    print("Number of steps:", number_of_steps_away(steps))
    print("Max steps:", max_number_of_steps(steps))
