import argparse
import sys
import re
import os, os.path
import math
import aoc_utils as utils

f = open("input25.txt", "r")
text = f.read()
parts = text.split('\n\n')

keys = []
locks = []

for part in parts:
    tumblers = [0,0,0,0,0]
    lines = part.split('\n')
    for y in range(1,6):
        for x in range(5):
            if lines[y][x] == '#':
                tumblers[x] += 1

    if lines[0] == '.....':
        keys.append(tumblers)
    else:
        locks.append(tumblers)


def main():
    the_sum = 0
    for key in keys:
        for lock in locks:
            fit = True
            for x in range(5):
                if key[x] + lock[x] > 5:
                    fit = False
            if fit:
                the_sum += 1
    print(the_sum)


if __name__ == "__main__":
    main()
