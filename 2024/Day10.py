import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input10.txt", "r")
    text = f.read()
    the_map = text.split('\n')
    map_copy = the_map.copy()
    width = len(the_map[0])
    height = len(the_map)
    the_sum = 0

    sys.setrecursionlimit(100000)

    for y in range(height):
        for x in range(width):
            if the_map[y][x] == '0':
                result = recurse(x, y, 0, the_map)
                the_sum += len(result)
    print(f'Sum: {the_sum}')


def recurse(x, y, h, the_map):
    if h == 9:
        return [f'{x}_{y}']
    width = len(the_map[0])
    height = len(the_map)
    result = []
    if x > 0:
        if int(the_map[y][x-1]) == h + 1:
            res = recurse(x - 1, y, h + 1, the_map)
            result.extend(res)
    if x < width - 1:
        if int(the_map[y][x+1]) == h + 1:
            res = recurse(x + 1, y, h + 1, the_map)
            result.extend(res)
            # for r in res:
            #     if r not in result:
            #         result.append(r)
    if y > 0:
        if int(the_map[y-1][x]) == h + 1:
            res = recurse(x, y - 1, h + 1, the_map)
            result.extend(res)
            # for r in res:
            #     if r not in result:
            #         result.append(r)
    if y < height - 1:
        if int(the_map[y+1][x]) == h + 1:
            res = recurse(x, y + 1, h + 1, the_map)
            result.extend(res)
            # for r in res:
            #     if r not in result:
            #         result.append(r)
    return result


if __name__ == "__main__":
    main()
