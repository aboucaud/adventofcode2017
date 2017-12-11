"""
http://adventofcode.com/2017/day/11

--- Day 11: Hex Ed ---

Crossing the bridge, you've barely reached the other side of the stream when a program comes up to you, clearly in distress. "It's my child process," she says, "he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be found to the north, northeast, southeast, south, southwest, and northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \
You have the path the child process took. Starting where he started, you need to determine the fewest number of steps required to reach him. (A "step" means to move from the hex you are in to any adjacent hex.)

For example:

ne,ne,ne is 3 steps away.
ne,ne,sw,sw is 0 steps away (back where you started).
ne,ne,s,s is 2 steps away (se,se).
se,sw,se,sw,sw is 3 steps away (s,s,sw).

--- Part Two ---

How many steps away is the furthest he ever got from his starting position?

"""
from typing import NamedTuple, List


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
    for idx in range(1, len(paths)+1):
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
