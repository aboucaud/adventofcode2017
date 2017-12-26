"""
http://adventofcode.com/2017/day/25
"""
from typing import NamedTuple, List, Dict, Tuple

from collections import defaultdict


State = NamedTuple('State', [('val', int),
                             ('step', int),
                             ('next_state', str)])
StateDict = Dict[str, Tuple[State, State]]


def parse_input(input: List[str]) -> Tuple[StateDict, str, int]:
    start = input[0].split()[-1][0]
    steps = int(input[1].split()[-2])
    split_input = [line.split()[-1][:-1]
                   for line in input
                   if line]
    clean_input = [e.replace('right', '1').replace('left', '-1')
                   for e in split_input]
    inp = clean_input[2:]

    states = {}
    for i in range(0, len(inp), 9):
        states[inp[i]] = (State(int(inp[i + 2]), int(inp[i + 3]), inp[i + 4]),
                          State(int(inp[i + 6]), int(inp[i + 7]), inp[i + 8]))

    return states, start, steps


def checksum(states: StateDict,
             start_state: str,
             max_steps: int) -> int:
    tape = defaultdict(int)  # type: Dict[int, int]
    pos = 0
    n_iter = 0
    current_state = start_state
    while n_iter < max_steps:
        s = states[current_state][tape[pos]]
        tape[pos] = s.val
        pos += s.step
        current_state = s.next_state

        n_iter += 1

    return sum(tape.values())


TEST = """Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.""".splitlines()
assert checksum(*parse_input(TEST)) == 3


if __name__ == '__main__':
    with open('day25_input.txt', 'r') as f:
        INPUT = f.read().splitlines()
    print('Checksum:', checksum(*parse_input(INPUT)))
