"""
http://adventofcode.com/2017/day/21
"""
from typing import List, Dict, Union

import numpy as np

PUZZLE = """.#.
..#
###""".splitlines()


def parse_input(recipe: List[str]) -> Dict[str, str]:
    rule_book = {}
    for line in recipe:
        rule, output = line.split(' => ')
        rules = rotate_and_flip(rule)
        for r in rules:
            rule_book[r] = output
    return rule_book


def rotate_and_flip(rule: str) -> List[str]:
    grid = [list(line) for line in rule.split('/')]
    size = len(grid)

    rgrids = []
    for i in range(4):
        rotated_grid = np.rot90(grid, i)
        rgrids.append(rotated_grid.tolist())
        rgrids.append(np.fliplr(rotated_grid).tolist())
        rgrids.append(np.flipud(rotated_grid).tolist())

    packed_rgrids = set([to_string(r) for r in rgrids])

    # Remove duplicates
    return list(packed_rgrids)


def to_string(rule: List[List[str]]) -> str:
    return '/'.join(''.join(row) for row in rule)


def enhance_grid(grid: List[str],
                 rule_book: Dict[str, str]) -> List[List[str]]:
    size = len(grid)
    if size % 2 == 0:
        step = 2
    else:
        step = 3

    new_grid = []
    for row in range(0, size, step):
        new_row = []
        for col in range(0, size, step):
            rule = '/'.join(''.join(grid[row + i][col + j]
                                    for j in range(step))
                            for i in range(step))
            new_row.append(rule_book[rule])
        new_grid.append(new_row)

    new_grid = join_squares(new_grid, step + 1)

    return new_grid


def join_squares(squares: List[List[str]], step: int) -> List[str]:
    grid = []
    size = len(squares)
    for row in range(size):
        srow = squares[row]
        grid.extend([''.join(col.split('/')[i] for col in srow)
                     for i in range(step)])

    return grid


def enhancement(grid: List[str],
                rules: Dict[str, str],
                reps: int = 1) -> List[str]:
    n_iter = 0
    while n_iter < reps:
        if n_iter > 0:
            grid = enhance_grid(grid, rules)
        else:
            grid = to_string(grid)
            grid = rules[grid].split('/')

        # print(f"Iter: {n_iter}\tPixels:", count_pixels(grid))
        n_iter += 1

    return grid


def count_pixels(grid: List[str]) -> int:
    return ''.join(grid).count('#')


def print_grid(grid: List[str]) -> None:
    print('\n'.join(grid))


TEST = ["../.# => ##./#../...",
        ".#./..#/### => #..#/..../..../#..#"]
rule_dict_test = parse_input(TEST)
assert count_pixels(enhancement(PUZZLE, rule_dict_test, 2)) == 12


if __name__ == '__main__':
    with open('day21_input.txt', 'r') as f:
        INPUT = f.read().splitlines()
    rule_dict = parse_input(INPUT)
    print(count_pixels(enhancement(PUZZLE, rule_dict, 5)))
    print(count_pixels(enhancement(PUZZLE, rule_dict, 18)))
