"""
http://adventofcode.com/2017/day/16
"""
from typing import List, Dict


def program_dance(programs: str, actions: List[str]) -> str:
    sequence = list(programs)
    for action in actions:
        if action.startswith('s'):
            spin(sequence, int(action[1:]))
        elif action.startswith('x'):
            ida, idb = action[1:].split('/')
            exchange(sequence, int(ida), int(idb))
        elif action.startswith('p'):
            pga, pgb = action[1:].split('/')
            partner(sequence, pga, pgb)
        else:
            print("Undefined action")

    return ''.join(sequence)


def spin(sequence: List[str], moves: int) -> None:
    sequence[:] = sequence[-moves:] + sequence[:-moves]


def exchange(sequence: List[str], id_a: int, id_b: int) -> None:
    sequence[id_a], sequence[id_b] = sequence[id_b], sequence[id_a]


def partner(sequence: List[str], pga: str, pgb: str) -> None:
    id_a = sequence.index(pga)
    id_b = sequence.index(pgb)
    sequence[id_a], sequence[id_b] = pgb, pga


def cycle_dance(programs: str, actions: List[str]) -> str:
    seen: List = []
    reps = 1000000000
    for i in range(reps):
        if programs in seen:
            return seen[reps % i]
        seen.append(programs)
        programs = program_dance(programs, actions)

    return programs


TEST = 'abcde'
assert program_dance(TEST, ['s1']) == 'eabcd'
assert program_dance(TEST, ['s1', 'x3/4']) == 'eabdc'
assert program_dance(TEST, ['s1', 'x3/4', 'pe/b']) == 'baedc'
assert cycle_dance(TEST, ['s1', 'x3/4', 'pe/b']) == 'abcde'


with open('day16_input.txt', 'r') as f:
    ACTIONS = f.read().strip().split(',')
programs = 'abcdefghijklmnop'
print('Final order:', program_dance(programs, ACTIONS))
print('Final order after a billion iterations:',
      cycle_dance(programs, ACTIONS))
