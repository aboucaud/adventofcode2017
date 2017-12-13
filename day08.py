"""
http://adventofcode.com/2017/day/8
"""
from typing import Tuple, List, Dict


def parse_line(line: str, registry: Dict[str, int]) -> None:
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

# Part2
# -----

def largest_value_ever(lines: List[str]) -> int:
    registry = initialize_variables(lines)
    max_val = -999
    for line in lines:
        parse_line(line, registry)
        max_val = max(max_val, max(registry.values()))

    return max_val


TEST = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""".split('\n')

assert largest_value(TEST) == 1
assert largest_value_ever(TEST) == 10


if __name__ == '__main__':
    with open('day08_input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    print('Largest value in registry:', largest_value(lines))
    print('Largest value ever in registry:', largest_value_ever(lines))
