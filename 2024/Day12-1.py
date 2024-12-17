import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input12.txt", "r")
    text = f.read()
    the_map = text.split('\n')
    the_sum = 0
    width = len(the_map[0])
    height = len(the_map)
    used = []

    for y in range(height):
        for x in range(width):
            result = recurse(x, y, the_map[y][x], the_map, used)
            the_sum += result[0] * result[1]

    print(f'Sum: {the_sum}')


def recurse(x, y, crop, the_map, used):
    width = len(the_map[0])
    height = len(the_map)
    if x < 0 or y < 0 or x > width - 1 or y > height - 1:
        return [0, 1]
    if crop != the_map[y][x]:
        return [0, 1]
    if f'{x}_{y}' in used:
        return [0, 0]

    used.append(f'{x}_{y}')
    result = []
    result.append(recurse(x, y+1, crop, the_map, used))
    result.append(recurse(x, y-1, crop, the_map, used))
    result.append(recurse(x+1, y, crop, the_map, used))
    result.append(recurse(x-1, y, crop, the_map, used))

    area = 1
    fence = 0
    for res in result:
        fence += res[1]
        area += res[0]
    return [area, fence]


if __name__ == "__main__":
    main()
