import argparse
import sys
import re
import os, os.path
import math
import aoc_utils as utils

f = open("input20.txt", "r")
text = f.read()
map1 = text.split('\n')
width = len(map1[0])
height = len(map1)

for y in range(height):
    for x in range(width):
        if map1[y][x] == 'E':
            end = [x, y]
        elif map1[y][x] == 'S':
            start = [x, y]


def main():
    sn = f'{start[0]}_{start[1]}'
    en = f'{end[0]}_{end[1]}'
    lengths = {}
    sys.setrecursionlimit(10000)
    move(map1, start[0], start[1], 0, lengths)

    the_sum = 0
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            if map1[y][x] == '#':
                y0 = y - 1
                y1 = y + 1
                x0 = x - 1
                x1 = x + 1
                diff = 0
                if map1[y0][x] == '.' and map1[y1][x] == '.':
                    diff = lengths[f'{x}_{y0}'] - lengths[f'{x}_{y1}']
                if map1[y][x0] == '.' and map1[y][x1] == '.':
                    diff = lengths[f'{x0}_{y}'] - lengths[f'{x1}_{y}']
                if diff != 0:
                    cheat = abs(diff) - 1
                    if cheat >= 100:
                        the_sum += 1

    print(the_sum)

    the_sum = 0
    n_points = len(lengths)
    keys = list(lengths.keys())
    for i in range(n_points-1):
        print(i)
        for j in range(i+1, n_points):
            pos1 = [int(t) for t in keys[i].split('_')]
            pos2 = [int(t) for t in keys[j].split('_')]
            dist = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
            if 1 < dist <= 20:
                diff = abs(lengths[keys[i]] - lengths[keys[j]])
                cheat = diff - dist + 1
                if cheat >= 100:
                    the_sum += 1

    print(the_sum)


def move(the_map, x, y, l, lengths):
    while not (x == end[0] and y == end[1]):
        name = f'{x}_{y}'
        if name in lengths.keys():
            exit(17)
        lengths[name] = l

        if the_map[y][x+1] in '.E' and f'{x+1}_{y}' not in lengths.keys():
            x += 1
        elif the_map[y][x-1] in '.E' and f'{x-1}_{y}' not in lengths.keys():
            x -= 1
        elif the_map[y+1][x] in '.E' and f'{x}_{y+1}' not in lengths.keys():
            y += 1
        elif the_map[y-1][x] in '.E' and f'{x}_{y-1}' not in lengths.keys():
            y -= 1

        l += 1
    lengths[f'{end[0]}_{end[1]}'] = l


if __name__ == "__main__":
    main()
