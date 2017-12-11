"""
http://adventofcode.com/2017/day/7

--- Day 7: Recursive Circus ---

Wandering further through the circuits of the computer, you come upon a tower of programs that have gotten themselves into a bit of trouble. A recursive algorithm has gotten out of hand, and now they're balanced precariously in a large tower.

One program at the bottom supports the entire tower. It's holding a large disc, and on the disc are balanced several more sub-towers. At the bottom of these sub-towers, standing on the bottom disc, are other programs, each holding their own disc, and so on. At the very tops of these sub-sub-sub-...-towers, many programs stand simply keeping the disc below them balanced but with no disc of their own.

You offer to help, but first you need to understand the structure of these towers. You ask each program to yell out their name, their weight, and (if they're holding a disc) the names of the programs immediately above them balancing on that disc. You write this information down (your puzzle input). Unfortunately, in their panic, they don't do this in an orderly fashion; by the time you're done, you're not sure which program gave which information.

For example, if your list is the following:

pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
...then you would be able to recreate the structure of the towers that looks like this:

                gyxo
              /
         ugml - ebii
       /      \
      |         jptl
      |
      |         pbga
     /        /
tknk --- padx - havc
     \        \
      |         qoyq
      |
      |         ktlj
       \      /
         fwft - cntj
              \
                xhth
In this example, tknk is at the bottom of the tower (the bottom program), and is holding up ugml, padx, and fwft. Those programs are, in turn, holding up other programs; in this example, none of those programs are holding up any other programs, and are all the tops of their own towers. (The actual tower balancing in front of you is much larger.)

Before you're ready to help them, you need to make sure your information is correct. What is the name of the bottom program?
"""
from typing import List, Dict, Tuple


TEST = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""


def current_program(line: str) -> str:
    return line.split(' (')[0]


def above_programs(line: str) -> List[str]:
    res = line.split(' -> ')
    if len(res) == 1:
        return []
    return res[1].split(', ')


def find_bottom_program(programs: List[str]) -> str:
    program_list = [current_program(line) for line in programs]
    above_program_list = []
    for line in programs:
        above_program_list.extend(above_programs(line))

    not_above_program = set(program_list) - set(above_program_list)

    if len(not_above_program) == 1:
        return not_above_program.pop()

    return ''


assert find_bottom_program(TEST.split('\n')) == 'tknk'


def parse_line(line: str) -> Tuple[str, int, List[str]]:
    res = line.split(' -> ')
    name, weight = res[0].split()
    weight = weight.lstrip('(').rstrip(')')
    aboves = [] if len(res) == 1 else res[1].split(', ')

    return (name, int(weight), aboves)


def parse_programs(programs: List[str]) -> Tuple[Dict[str, int], Dict[str, List[str]]]:
    weights_dict = {}
    aboves_dict = {}
    for line in programs:
        name, weight, aboves = parse_line(line)
        weights_dict[name] = weight
        aboves_dict[name] = aboves
    return (weights_dict, aboves_dict)


def find_unbalanced_weight(programs: List[str]):
    main_prog = find_bottom_program(programs)
    weights, aboves = parse_programs(programs)

    def compute_weight(prog):
        subweight = { name: compute_weight(name) for name in aboves[prog] }
        sub = { weight for weight, _ in subweight.values()}
        is_balanced = len(sub) <= 1
        weight = weights[prog] + sum(weight for weight, _ in subweight.values())

        if len(sub) > 1 and all(is_balanced for _, is_balanced in subweight.values()):
            print("Name:", prog)

            for name, (total_weight, is_balanced) in subweight.items():
                print(name, total_weight, weights[name])

        return weight, is_balanced

    compute_weight(main_prog)
    # for prog in aboves['ihnus']:
        # print(prog, compute_weight(prog))
    # print(compute_weight('ljaktj'))
    # [compute_weight(prog) for prog in aboves[main_prog]])

# assert find_unbalanced_weight(TEST.split('\n')) == [243, 243, 251]
# find_unbalanced_weight(TEST.split('\n'))


if __name__ == '__main__':
    with open('day07_input.txt', 'r') as f:
        programs = [line.strip() for line in f]
    print("Name of bottom program:", find_bottom_program(programs))
    print("Weight of child programs:", find_unbalanced_weight(programs))
