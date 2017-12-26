"""
http://adventofcode.com/2017/day/10
"""
from typing import List


def hash_function(lengths: List[int], size: int = 256) -> List[int]:
    marks = list(range(size))
    current_pos = 0
    skip_size = 0

    for length in lengths:
        current_pos = current_pos % size
        end_pos = current_pos + length
        cycle_pos = 0
        if end_pos >= size:
            cycle_pos = end_pos % size
            end_pos = size

        list_to_reverse = marks[current_pos:end_pos] + marks[:cycle_pos]
        new_list = list(reversed(list_to_reverse))

        marks[current_pos:end_pos] = new_list[:length - cycle_pos]
        marks[:cycle_pos] = new_list[length - cycle_pos:]

        current_pos += length
        current_pos += skip_size
        skip_size += 1

    return marks


assert hash_function([3, 4, 1, 5], size=5) == [3, 4, 2, 1, 0]


def first_two_numbers(lengths: List[int], size: int = 256) -> int:
    marks = hash_function(lengths, size)
    return marks[0] * marks[1]


assert first_two_numbers([3, 4, 1, 5], size=5) == 12


def read_input(text: str) -> List[int]:
    """
    Convert string of characters to their ASCII representation
    """
    lengths = [ord(c) for c in text]
    lengths += [17, 31, 73, 47, 23]
    return lengths


def sparse_hash(lengths: List[int]) -> List[int]:
    size = 256
    marks = list(range(size))
    current_pos = 0
    skip_size = 0

    for _ in range(64):
        for length in lengths:
            current_pos = current_pos % size
            end_pos = current_pos + length
            cycle_pos = 0
            if end_pos >= size:
                cycle_pos = end_pos % size
                end_pos = size

            list_to_reverse = marks[current_pos:end_pos] + marks[:cycle_pos]
            new_list = list(reversed(list_to_reverse))

            marks[current_pos:end_pos] = new_list[:length - cycle_pos]
            marks[:cycle_pos] = new_list[length - cycle_pos:]

            current_pos += length
            current_pos += skip_size
            skip_size += 1

    return marks


def dense_hash(marks: List[int]) -> List[int]:
    assert len(marks) == 256
    hash = []
    id_start = 0
    id_end = 16
    for _ in range(16):
        submark = marks[id_start:id_end]
        res = eval(' ^ '.join(str(val) for val in submark))
        hash.append(res)
        id_start = id_end
        id_end += 16

    return hash


def to_hex_string(hash: List[int]) -> str:
    return ''.join('{:02x}'.format(val) for val in hash)


def knot_hash(puzzle: str) -> str:
    lengths = read_input(puzzle)
    marks = sparse_hash(lengths)
    d_hash = dense_hash(marks)
    return to_hex_string(d_hash)


assert knot_hash("") == 'a2582a3a0e66e6e86e3812dcb672a272'
assert knot_hash("AoC 2017") == '33efeb34ea91902bb2f59c9920caa6cd'
assert knot_hash("1,2,3") == '3efbe78a8d82f29979031a4aa0b16a9d'
assert knot_hash("1,2,4") == '63960835bcdc130f0b66d7ff4f6a5a8e'


if __name__ == '__main__':
    with open('day10_input.txt', 'r') as f:
        INPUT = f.read().strip()
    lengths = [int(num) for num in INPUT.split(',')]
    print("Value:", first_two_numbers(lengths, size=256))
    print("Knot hash:", knot_hash(INPUT))
