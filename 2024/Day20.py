import argparse
import sys
import re
import os, os.path
import math
import aoc_utils as utils

f = open("input20.txt", "r")
text = f.read()
lines = text.split('\n')
falling = [x.split(',') for x in lines]



def main():
    line = '.' * 71
    the_map = [line] * 71
    width = len(the_map[0])
    height = len(the_map)
    sys.setrecursionlimit(100000)
    for t in range(1024):
        utils.set_point(the_map, int(falling[t][0]), int(falling[t][1]), '#')

    memo_map = {}
    move(the_map, 0, 0, 0, memo_map)
    utils.print_map(the_map)
    name = f'{width-1}_{height-1}'
    print(memo_map[name])

    for t in range(1024, 2524):
        utils.set_point(the_map, int(falling[t][0]), int(falling[t][1]), '#')

    for t in range(2524, len(falling)):
        utils.set_point(the_map, int(falling[t][0]), int(falling[t][1]), '#')
        memo_map = {}
        move(the_map, 0, 0, 0, memo_map)
        if name in memo_map.keys():
            print(memo_map[name])
        else:
            print(f'Coords for t = {t}: {falling[t][0]},{falling[t][1]}')
            break

def move(the_map, x, y, path, memo_map):
    width = len(the_map[0])
    height = len(the_map)
    if x < 0 or y < 0 or x > width - 1 or y > height - 1:
        return
    if the_map[y][x] == '#':
        return
    name = f'{x}_{y}'
    if name in memo_map.keys():
        if memo_map[name] > path:
            memo_map[name] = path
        else:
            return
    else:
        memo_map[name] = path

    if x == width - 1 and y == height - 1:
        return

    down = move(the_map, x, y + 1, path + 1, memo_map)
    right = move(the_map, x + 1, y, path + 1, memo_map)
    up = move(the_map, x, y - 1, path + 1, memo_map)
    left = move(the_map, x - 1, y, path + 1, memo_map)


if __name__ == "__main__":
    main()
