"""
http://adventofcode.com/2017/day/8

--- Day 8: I Heard You Like Registers ---

You receive a signal directly from the CPU. Because of your recent assistance with jump instructions, it would like you to compute the result of a series of unusual register instructions.

Each instruction consists of several parts: the register to modify, whether to increase or decrease that register's value, the amount by which to increase or decrease it, and a condition. If the condition fails, skip the instruction without modifying the register. The registers all start at 0. The instructions look like this:

b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
These instructions would be processed as follows:

Because a starts at 0, it is not greater than 1, and so b is not modified.
a is increased by 1 (to 1) because b is less than 5 (it is 0).
c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
c is increased by -20 (to -10) because c is equal to 10.
After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to). However, the CPU doesn't have the bandwidth to tell you what all the registers are named, and leaves that to you to determine.

What is the largest value in any register after completing the instructions in your puzzle input?

"""
from typing import Tuple, List, Dict


def parse_line(line: str, registry: Dict[str, int]) -> None:
    """
    """
    name, instr, val, _, name2, cond, val2 = line.split()

    if eval('registry["{}"] {} {}'.format(name2, cond, val2)):
        if instr == 'inc':
            registry[name] += int(val)
        else:
            registry[name] -= int(val)


def initialize_variables(lines: List[str]) -> Dict[str, int]:
    registry = {}
    variables = set()
    for line in lines:
        variables.add(line.split()[0])

    for name in variables:
        registry[name] = 0

    return registry


def largest_value(lines: List[str]) -> int:
    registry = initialize_variables(lines)
    for line in lines:
        parse_line(line, registry)

    return max(registry.values())


TEST = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""


assert largest_value(TEST.split('\n')) == 1


def largest_value_ever(lines: List[str]) -> int:
    registry = initialize_variables(lines)
    max_val = -999
    for line in lines:
        parse_line(line, registry)
        max_val = max(max_val, max(registry.values()))

    return max_val


assert largest_value_ever(TEST.split('\n')) == 10


if __name__ == '__main__':
    with open('day08_input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    print('Largest value in registry:', largest_value(lines))
    print('Largest value ever in registry:', largest_value_ever(lines))
