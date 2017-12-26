"""

"""
from typing import List

from collections import Counter


def valid_passphrase(phrase: str) -> bool:
    counter = Counter(phrase.split())
    for val in counter.values():
        if val > 1:
            return False
    return True


assert valid_passphrase("aa bb cc dd ee")
assert not valid_passphrase("aa bb cc dd aa")
assert valid_passphrase("aa bb cc dd ee aaa")


def count_valid(passphrases: List[str]) -> int:
    return sum(valid_passphrase(phrase)
               for phrase in passphrases)

# Part 2
# ------


def valid_passphrase_anagram(phrase: str) -> bool:
    """
    Trick for anagrams : sorted words are the same
    """
    words = phrase.split()
    word_set = set(tuple(sorted(word)) for word in words)
    return len(words) == len(word_set)


assert valid_passphrase_anagram("abcde fghij")
assert not valid_passphrase_anagram("abcde xyz ecdab")
assert valid_passphrase_anagram("a ab abc abd abf abj")
assert valid_passphrase_anagram("iiii oiii ooii oooi oooo")
assert not valid_passphrase_anagram("oiii ioii iioi iiio")


def count_valid_stronger(passphrases: List[str]) -> int:
    return sum(valid_passphrase(phrase) & valid_passphrase_anagram(phrase)
               for phrase in passphrases)


if __name__ == '__main__':
    with open('day04_input.txt', 'r') as f:
        PASSPHRASES = f.read().splitlines()
    print("Count:", count_valid(PASSPHRASES))
    print("Count 2:", count_valid_stronger(PASSPHRASES))
