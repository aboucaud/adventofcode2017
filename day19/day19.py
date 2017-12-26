"""
http://adventofcode.com/2017/day/19
"""
from typing import List, Tuple


def chain(maze: List[str]) -> Tuple[str, int]:
    r = 0
    c = maze[r].index('|')
    end_of_path = False
    direction = 'down'
    letters = []
    length = 0
    while not end_of_path:
        val = maze[r][c]
        if val.isalpha():
            letters.append(val)
        elif val == '+':
            direction = change_direction(direction, maze, (r, c))
        elif val == ' ':
            end_of_path = True

        if direction == 'down':
            r += 1
        elif direction == 'up':
            r -= 1
        elif direction == 'left':
            c -= 1
        elif direction == 'right':
            c += 1

        length += 1

    return ''.join(letters), length - 1


def change_direction(direction: str,
                     maze: List[str],
                     coords: Tuple[int, int]) -> str:
    r, c = coords
    if direction in ['up', 'down']:
        if maze[r][c + 1] == ' ':
            newdir = 'left'
        else:
            newdir = 'right'
    else:
        if maze[r + 1][c] == ' ':
            newdir = 'up'
        else:
            newdir = 'down'

    return newdir


TEST = """.....|..........
.....|..+--+....
.....A..|..C....
.F---|----E|--+.
.....|..|..|..D.
.....+B-+..+--+.
................""".replace('.', ' ').splitlines()
assert chain(TEST)[0] == 'ABCDEF'
assert chain(TEST)[1] == 38


with open('day19_input.txt', 'r') as f:
    INPUT = f.read().splitlines()
    print("Chain:", chain(INPUT)[0])
    print("Length:", chain(INPUT)[1])
