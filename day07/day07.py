"""
http://adventofcode.com/2017/day/7
"""
from typing import List, Dict, Tuple


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

# Part2
# -----


def parse_line(line: str) -> Tuple[str, int, List[str]]:
    res = line.split(' -> ')
    name, weight = res[0].split()
    weight = weight.lstrip('(').rstrip(')')
    aboves = [] if len(res) == 1 else res[1].split(', ')

    return (name, int(weight), aboves)


def parse_programs(programs: List[str]) -> Tuple[Dict[str, int],
                                                 Dict[str, List[str]]]:
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
        subweight = {name: compute_weight(name) for name in aboves[prog]}
        sub = {weight for weight, _ in subweight.values()}
        is_balanced = len(sub) <= 1
        weight = weights[prog] + sum(weight
                                     for weight, _ in subweight.values())

        if len(sub) > 1 and all(is_balanced
                                for _, is_balanced in subweight.values()):
            print("\nTop program:", prog)
            print("Name:", "Weight:", "Total weight:", sep='\t')
            for name, (total_weight, is_balanced) in subweight.items():
                print(name, weights[name], total_weight, sep='\t')

        return weight, is_balanced

    compute_weight(main_prog)


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
cntj (57)""".split('\n')

assert find_bottom_program(TEST) == 'tknk'
# find_unbalanced_weight(TEST)

if __name__ == '__main__':
    with open('day07_input.txt', 'r') as f:
        programs = f.read().splitlines()
    print("Name of bottom program:", find_bottom_program(programs))
    print("Weight of child programs:", find_unbalanced_weight(programs))
