"""
http://adventofcode.com/2017/day/12
"""
from typing import List, Dict, Set


def parse_inputs(input: List[str]) -> Dict[int, List[int]]:
    new_list = [line.split(' <-> ') for line in input]
    return {int(pid): [int(v) for v in val.split(',')]
            for pid, val in new_list}


def connected_programs(record: Dict[int, List[int]], prog_id: int) -> Set[int]:
    ids = [prog_id]
    programs = set()

    while ids:
        current_id = ids.pop()
        programs.add(current_id)
        for next_id in record[current_id]:
            if next_id not in programs and next_id not in ids:
                ids.append(next_id)

    return programs


def how_many_programs(input: List[str], prog_id: int = 0) -> int:
    record = parse_inputs(input)
    programs = connected_programs(record, prog_id)

    return len(programs)

# Part2
# -----


def how_many_groups(input: List[str]) -> int:
    record = parse_inputs(input)
    seen: Set[int] = set()
    groups = 0

    for i in range(len(record)):
        if i in seen:
            continue
        groups += 1
        seen.add(i)
        seen.update(connected_programs(record, i))

    return groups


TEST = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5""".split('\n')

assert how_many_programs(TEST, prog_id=0) == 6
assert how_many_groups(TEST) == 2


if __name__ == '__main__':
    with open('day12_input.txt', 'r') as f:
        lines = f.read().splitlines()
    print("There are {} programs in prog id 0.".format(
          how_many_programs(lines, prog_id=0)))
    print("There are {} groups.".format(
          how_many_groups(lines)))
