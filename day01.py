"""
http://adventofcode.com/2017/day/1
"""

def sum_captcha(s: str, halfway: bool = False) -> int:
    if not halfway:
        second_list = s[1:] + s[0]
    else:
        half = int(len(s) / 2)
        second_list = s[half:] + s[:half]

    total = 0
    for val, next_val in zip(s, second_list):
        if val == next_val:
            total += int(val)

    return total


assert sum_captcha("1122") == 3
assert sum_captcha("91212129") == 9
assert sum_captcha("1234") == 0
assert sum_captcha("1111") == 4

assert sum_captcha("1212", True) == 6
assert sum_captcha("1221", True) == 0
assert sum_captcha("123425", True) == 4
assert sum_captcha("123123", True) == 12
assert sum_captcha("12131415", True) == 4


if __name__ == "__main__":
    with open('day01_input.txt', 'r') as f:
        INPUT = f.read().strip()
    print("Sum consecutive:", sum_captcha(INPUT))
    print("Sum halfway around:", sum_captcha(INPUT, halfway=True))
