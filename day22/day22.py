"""
http://adventofcode.com/2017/day/22
"""
from typing import Dict, Tuple, List
from collections import defaultdict


def parse_input(grid: List[str]) -> Dict[Tuple[int, int], int]:
    nrow = len(grid)
    ncol = len(grid[0])
    rcent = nrow // 2
    ccent = ncol // 2

    new_grid: Dict[Tuple[int, int], int] = defaultdict(int)
    for i in range(nrow):
        for j in range(ncol):
            if grid[i][j] == '#':
                new_grid[(j - rcent, -i + ccent)] = 2

    return new_grid


class Direction:
    dirlist = ['up', 'right', 'down', 'left']

    def __init__(self, pos: str) -> None:
        self.pos = self.dirlist.index(pos)

    def turn_left(self):
        self.pos -= 1
        self.pos %= 4

    def turn_right(self):
        self.pos += 1
        self.pos %= 4

    @property
    def current(self) -> str:
        return self.dirlist[self.pos]


def bursts(input: List[str], reps: int) -> int:
    grid = parse_input(input)
    direction = Direction('up')
    x, y = 0, 0
    infection = 0

    n_iter = 0
    while n_iter < reps:
        if grid[(x, y)] == 2:
            direction.turn_right()
            grid[(x, y)] = 0
        else:
            direction.turn_left()
            grid[(x, y)] = 2
            infection += 1

        if direction.current == 'up':
            y += 1
        elif direction.current == 'down':
            y -= 1
        elif direction.current == 'left':
            x -= 1
        elif direction.current == 'right':
            x += 1

        n_iter += 1

    return infection


def bursts2(input: List[str], reps: int) -> int:
    grid = parse_input(input)
    x, y = 0, 0
    direction = Direction('up')
    infection = 0

    n_iter = 0

    # Grid value
    # ----------
    # 0: clean, 1: weakened, 2: infected, 3: flagged
    while n_iter < reps:
        if grid[(x, y)] == 0:
            direction.turn_left()
        elif grid[(x, y)] == 1:
            infection += 1
        elif grid[(x, y)] == 2:
            direction.turn_right()
        elif grid[(x, y)] == 3:
            direction.turn_right()
            direction.turn_right()

        grid[(x, y)] += 1
        grid[(x, y)] %= 4

        if direction.current == 'up':
            y += 1
        elif direction.current == 'down':
            y -= 1
        elif direction.current == 'left':
            x -= 1
        elif direction.current == 'right':
            x += 1

        n_iter += 1

    return infection


TEST = """..#
#..
...""".splitlines()
assert bursts(TEST, 7) == 5
assert bursts2(TEST, 100) == 26
assert bursts2(TEST, 10000000) == 2511944


if __name__ == '__main__':
    with open('day22_input.txt', 'r') as f:
        INPUT = f.read().splitlines()
        print("Infection bursts:", bursts(INPUT, 10000))
        print("Infection bursts:", bursts2(INPUT, 10000000))
