"""
http://adventofcode.com/2017/day/2
"""
from typing import List


def parse_table(table: List[str]) -> List[List[int]]:
    return [[int(val) for val in row.split()]
            for row in table]


def row_checksum(table: List[str]) -> int:
    rows = parse_table(table)
    return sum(max(row) - min(row) for row in rows)

# Part2
# -----


def even_row_checksum(table: List[str]) -> int:
    rows = parse_table(table)
    return sum(get_dividers(row) for row in rows)


def get_dividers(row: List[int]) -> int:
    sorted_row = sorted(row)
    while sorted_row:
        num = sorted_row.pop()
        for val in sorted_row:
            if num % val == 0:
                return num // val
    return 0


assert row_checksum(["5 1 9 5", "7 5 3", "2 4 6 8"]) == 18
assert even_row_checksum(["5 9 2 8", "9 4 7 3", "3 8 6 5"]) == 9


if __name__ == "__main__":
    with open('day02_input.txt', 'r') as f:
        TABLE = f.read().splitlines()
    print("Checksum:", row_checksum(TABLE))
    print("Even checksum:", even_row_checksum(TABLE))
