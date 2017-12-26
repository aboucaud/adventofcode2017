"""
http://adventofcode.com/2017/day/24
"""
from typing import List


def parse_input(input: List[str]) -> List[List[int]]:
    return [list(map(int, line.split('/'))) for line in input]


def build_bridges(parts, pin, bridge):
    available_parts = [part for part in parts if pin in part]
    # print(f'Available parts = {available_parts}')
    if not available_parts:
        return [bridge]

    # print(f"bridge = {bridge}")
    output = []
    for part in available_parts:
        # print(f'Trying part {part}')
        parts_left = parts[:]
        parts_left.remove(part)
        pins = part[:]
        pins.remove(pin)
        # print(f'output = {output}')
        output += build_bridges( parts_left, pins[0], bridge + [part])

    return output


def strength(input, longest=False):
    parts = parse_input(input)
    bridges = build_bridges(parts, pin=0, bridge=[])
    scores = [sum([sum(part)
                   for part in b])
              for b in bridges]
    if longest:
        bridge_length = [len(b) for b in bridges]
        return max([(length, score)
                    for length, score in zip(bridge_length, scores)])

    return max(scores)


TEST = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10""".splitlines()
assert strength(TEST[:]) == 31
assert strength(TEST[:], longest=True)[1] == 19


if __name__ == '__main__':
    with open('day24_input.txt', 'r') as f:
        INPUT = f.read().splitlines()
    print("Max strength :", strength(INPUT[:]))
    print("Max length, strength :", strength(INPUT[:], longest=True))
