"""
http://adventofcode.com/2017/day/14
"""
from typing import List, Dict, Tuple


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


def to_hex(hash: List[int]) -> str:
    return ''.join('{:02x}'.format(val) for val in hash)


def knot_hash(puzzle: str) -> str:
    lengths = read_input(puzzle)
    marks = sparse_hash(lengths)
    d_hash = dense_hash(marks)
    return to_hex(d_hash)


def to_binary(hex_key: str) -> str:
    hex_scale = 16
    output_size = len(hex_key) * 4
    return bin(int(hex_key, hex_scale))[2:].zfill(output_size)


assert to_binary('0') == '0000'
assert to_binary('1') == '0001'
assert to_binary('e') == '1110'
assert to_binary('f') == '1111'


def render_disk(key: str) -> Dict[Tuple[int, int], int]:
    rows = ['{}-{}'.format(key, x) for x in range(128)]
    hashes = [knot_hash(row) for row in rows]
    brows = [to_binary(hash) for hash in hashes]
    disk = {(irow, icol): int(brows[irow][icol])
            for irow in range(128)
            for icol in range(128)}

    return disk


def pretty_disk(key: str) -> str:
    disk = render_disk(key)
    puzzle = '\n'.join([''.join([str(disk[(i, j)])
                                 for j in range(128)])
                        for i in range(128)])
    puzzle = puzzle.replace('0', '.')
    puzzle = puzzle.replace('1', '#')
    return puzzle


def how_many_squares(key: str) -> int:
    disk = render_disk(key)
    return sum(disk.values())


def how_many_regions(key: str) -> int:
    regions = 0
    neighbors = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    disk = render_disk(key)
    unseen = [key
              for key, val in disk.items()
              if val == 1]
    while unseen:
        queue = [unseen[0]]
        while queue:
            (x, y) = queue.pop()
            if (x, y) in unseen:
                unseen.remove((x, y))
                queue.extend([(x + dx, y + dy) for dx, dy in neighbors])
        regions += 1

    return regions


TEST = "flqrgnkx"
assert how_many_squares(TEST) == 8108
assert how_many_regions(TEST) == 1242


if __name__ == '__main__':
    with open('day14_input.txt', 'r') as f:
        DATA = f.read().strip()
    print("Number of used squares:", how_many_squares(DATA))
    print("Number of regions:", how_many_regions(DATA))
