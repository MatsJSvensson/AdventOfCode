import argparse
import sys
import re
import os, os.path
import math
import aoc_utils as utils

f = open("input19.txt", "r")
text = f.read()
parts = text.split('\n\n')
towels = parts[0].split(', ')
patterns = parts[1].split('\n')

towel_dict = {}
for towel in towels:
    l = len(towel)
    if l in towel_dict.keys():
        towel_dict[l].append(towel)
    else:
        towel_dict[l] = [towel]
max_length = max(towel_dict.keys())


def main():
    the_sum = 0
    other_sum = 0
    memo_dict = {}
    for pattern in patterns:
        res = pattern_match(pattern, memo_dict)
        if res:
            the_sum += 1
        other_sum += res
        print(the_sum)

    print(f'Sum: {the_sum}')
    print(f'Sum 2: {other_sum}')


def pattern_match(pattern, memo_dict):
    if pattern in memo_dict.keys():
        return memo_dict[pattern]
    length = len(pattern)
    if length == 0:
        return 1
    m = min(length, max_length)

    a_sum = 0
    for x in range(m, 0, -1):
        part = pattern[:x]
        if x in towel_dict.keys() and part in towel_dict[x]:
            new_pattern = pattern[x:]
            res = pattern_match(new_pattern, memo_dict)
            if res > 0:
                a_sum += res
            else:
                memo_dict[new_pattern] = 0
    memo_dict[pattern] = a_sum
    return a_sum


if __name__ == "__main__":
    main()
