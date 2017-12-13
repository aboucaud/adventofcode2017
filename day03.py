"""
http://adventofcode.com/2017/day/3

37  36  35  34  33  32  31
38  17  16  15  14  13  30
39  18   5   4   3  12  29
40  19   6   1   2  11  28
41  20   7   8   9  10  27
42  21  22  23  24  25  26
43  44  45  46  47 -->  ...

"""
from typing import Tuple, Iterator, Dict
import math
import itertools
from collections import defaultdict


def find_square_size(num: int) -> int:
    val = int(math.sqrt(num - 1))

    if val % 2 == 0:
        return val + 1

    return val + 2


assert find_square_size(9) == 3
assert find_square_size(24) == 5
assert find_square_size(25) == 5
assert find_square_size(26) == 7


def grid_position(num: int) -> Tuple[int, int]:
    if num == 1:
        return (0, 0)

    size = find_square_size(num)
    step = size - 1

    dist_to_first_corner = abs(size ** 2 - num)
    dist_to_next_corner = dist_to_first_corner % step
    # dist_to_closest_corner = abs(dist_to_next_corner - step // 2)
    corner_number = dist_to_first_corner // step
    # return step // 2 + dist_to_closest_corner
    pos = size // 2

    if corner_number == 0:
        loc = (pos - dist_to_next_corner, - pos)
    elif corner_number == 1:
        loc = (- pos, - pos + dist_to_next_corner)
    elif corner_number == 2:
        loc = (- pos + dist_to_next_corner, pos)
    elif corner_number == 3:
        loc = (pos, pos - dist_to_next_corner)
    else:
        raise ValueError("You should not end up here")

    return loc


assert grid_position(1) == (0, 0)
assert grid_position(2) == (1, 0)
assert grid_position(3) == (1, 1)
assert grid_position(4) == (0, 1)
assert grid_position(5) == (-1, 1)
assert grid_position(9) == (1, -1)
assert grid_position(10) == (2, -1)


def find_distance(num: int) -> int:
    dx, dy = grid_position(num)
    return abs(dx) + abs(dy)

assert find_distance(1) == 0
assert find_distance(12) == 3
assert find_distance(23) == 2
assert find_distance(1024) == 31


def get_neighbours(loc: Tuple[int, int]) -> Iterator[Tuple[int, int]]:
    x, y = loc
    yield x + 1, y
    yield x + 1, y + 1
    yield x, y + 1
    yield x - 1, y + 1
    yield x - 1, y
    yield x - 1, y - 1
    yield x, y - 1
    yield x + 1, y - 1


def first_value_larger_than(num: int) -> int:
    square_dict: Dict[Tuple[int, int], int] = defaultdict(int)

    square_dict[(0, 0)] = 1

    for i in itertools.count(2):
        loc = grid_position(i)
        val = sum(square_dict[neighbour]
                  for neighbour in get_neighbours(loc))
        if val > num:
            return val

        square_dict[loc] = val

    print(square_dict)
    return -1


if __name__ == '__main__':
    with open('day03_input.txt', 'r') as f:
        NUMBER = int(f.read().strip())
    print("Distance:", find_distance(NUMBER))
    print("Larget val:", first_value_larger_than(NUMBER))
