"""
http://adventofcode.com/2017/day/9
"""
from typing import List, Dict, Tuple


def parse_stream(stream: str) -> int:
    score = 0
    group = 0
    cancel = False
    in_garbage = False

    for v in stream:
        if cancel:
            cancel = False
            continue
        if v == '!':
            cancel = True
            continue
        if v == '<':
            in_garbage = True
            continue
        if in_garbage:
            if v == '>':
                in_garbage = False
            continue
        if v == '{':
            group += 1
        if v == '}':
            score += group
            group -= 1

    return score


assert parse_stream("{}") == 1
assert parse_stream("{{{}}}") == 6
assert parse_stream("{{},{}}") == 5
assert parse_stream("{{{},{},{{}}}}") == 16
assert parse_stream("{<a>,<a>,<a>,<a>}") == 1
assert parse_stream("{{<ab>},{<ab>},{<ab>},{<ab>}}") == 9
assert parse_stream("{{<!!>},{<!!>},{<!!>},{<!!>}}") == 9
assert parse_stream("{{<a!>},{<a!>},{<a!>},{<ab>}}") == 3


def parse_stream_with_garbage(stream: str) -> int:
    score = 0
    cancel = False
    in_garbage = False

    for v in stream:
        if cancel:
            cancel = False
            continue
        if v == '!':
            cancel = True
            continue
        if in_garbage:
            if v == '>':
                in_garbage = False
                continue
            score += 1
        if v == '<':
            in_garbage = True
            continue

    return score


assert parse_stream_with_garbage("<>") == 0
assert parse_stream_with_garbage("<random characters>") == 17
assert parse_stream_with_garbage("<<<<>") == 3
assert parse_stream_with_garbage("<{!>}>") == 2
assert parse_stream_with_garbage("<!!>") == 0
assert parse_stream_with_garbage("<!!!>>") == 0
assert parse_stream_with_garbage("<{o'i!a,<{i<a>") == 10


if __name__ == '__main__':
    with open('day09_input.txt', 'r') as f:
        groups = [line.strip() for line in f]
    total_score = sum(parse_stream(line) for line in groups)
    total_garbage = sum(parse_stream_with_garbage(line) for line in groups)
    print("Total score:", total_score)
    print("Total garbage:", total_garbage)
