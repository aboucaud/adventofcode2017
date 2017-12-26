"""
http://adventofcode.com/2017/day/23
"""
from typing import List, Dict, NamedTuple, Tuple, Union

import math
from collections import defaultdict


Instruction = NamedTuple('Instruction', [('action', str),
                                         ('name', str),
                                         ('value', str)])


def parse_input(input: List[str]) -> List[Instruction]:
    instructions = []
    for line in input:
        inst = line.split()
        instructions.append(Instruction(*inst))

    return instructions


def play(instructions: List[Instruction],
         debug: bool = False) -> Union[Tuple[int, int], int]:
    assembly = defaultdict(int)  # type: Dict[str, int]
    if debug:
        assembly['a'] = 1
    count = 0

    counter = 0
    idx = 0
    while 0 <= idx < len(instructions):
        i = instructions[idx]

        try:
            val = int(i.value)
        except ValueError:
            val = assembly[i.value]

        if i.action == 'set':
            assembly[i.name] = val
        elif i.action == 'sub':
            assembly[i.name] -= val
        elif i.action == 'mul':
            assembly[i.name] *= val
            count += 1
        elif i.action == 'jnz':
            if assembly[i.name] != 0 or i.name == '1':
                idx += val
                continue

        idx += 1
        counter += 1
        if debug and counter > 1000100:
            break

    if debug:
        return assembly['b'], assembly['c']

    return count


def is_prime(n: int):
    """
    https://stackoverflow.com/a/18833870
    """
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def find_non_prime(instructions: List[Instruction]) -> int:
    """
    The algorithm behind the instructions is a counter of non prime numbers
    between two given values

    The set of instructions can be broken down into three nested loops.
    Concerning the registry values:
    - a is the trigger
    - b and c are the boundary values
    - d and e are looping values
    - f is a boolean value
    - g is a buffer value (can be easily discarded)
    - h is a counter

    """
    b, c = play(instructions, debug=True)

    return sum(not is_prime(x) for x in range(b, c + 1, 17))


if __name__ == '__main__':
    with open('day23_input.txt', 'r') as f:
        INPUT = parse_input(f.read().splitlines())
    print("Number of times 'mul' is invoked:", play(INPUT))
    print("Number of non prime values:", find_non_prime(INPUT))

