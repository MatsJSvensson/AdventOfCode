import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input11.txt", "r")
    text = f.read()
    stones = text.split(' ')
    memo_map = {}
    the_sum = 0

    for stone in stones:
        new_stones = recurse(stone, 75, memo_map)
        the_sum += new_stones

    print(f'Sum: {the_sum}')


def recurse(stone, t, memo_map):
    if t == 0:
        return 1

    stone = clean_leading_zeroes(stone)

    if stone in memo_map.keys():
        if t in memo_map[stone].keys():
            return memo_map[stone][t]
    else:
        memo_map[stone] = {}

    length = len(stone)
    if stone == '0':
        value = recurse('1', t-1, memo_map)
    elif length % 2 == 0:
        half = int(length/2)
        value = recurse(stone[:half], t-1, memo_map) + recurse(stone[half:], t-1, memo_map)
    else:
        num = int(stone) * 2024
        value = recurse(str(num), t-1, memo_map)

    memo_map[stone][t] = value
    return value


def clean_leading_zeroes(stone):
    num = int(stone)
    return str(num)


if __name__ == "__main__":
    main()
