import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input15.txt", "r")
    text = f.read()
    m, d = text.split('\n\n')
    a_map = m.split('\n')
    d = d.split('\n')
    steps = ''
    for part in d:
        steps += part
    the_sum = 0
    width = len(a_map[0])
    height = len(a_map)
    x0 = -1
    y0 = -1
    new_map = []

    for y in range(height):
        new_row = ''
        for x in range(width):
            if a_map[y][x] == '@':
                x0 = x * 2
                y0 = y
                new_row += '@.'
            elif a_map[y][x] == '.':
                new_row += '..'
            elif a_map[y][x] == '#':
                new_row += '##'
            elif a_map[y][x] == 'O':
                new_row += '[]'

    pos = [x0, y0]
    for step in steps:
        if step == '>':
            pos = move(pos, [1, 0], new_map, '@')
        if step == '<':
            pos = move(pos, [-1, 0], new_map, '@')
        if step == '^':
            pos = move(pos, [0, -1], new_map, '@')
        if step == 'v':
            pos = move(pos, [0, 1], new_map, '@')

    print(step)
    print_map(a_map)
    print('\n')

    for y in range(height):
        for x in range(width):
            if new_map[y][x] == '[':
                the_sum += x + 100 * y

    print(f'Sum: {the_sum}')


def move(pos, step, a_map, char):
    x = pos[0] + step[0]
    y = pos[1] + step[1]

    if a_map[y][x] == '.':
        set_point(a_map, x, y, char)
        set_point(a_map, pos[0], pos[1], '.')
        return [x, y]
    if a_map[y][x] == '#':
        return pos
    if a_map[y][x] == '[':
        move([x, y], step, a_map, '[')
        if a_map[y][x] == 'O':
            return pos
        else:
            set_point(a_map, x, y, char)
            set_point(a_map, pos[0], pos[1], '.')
            return [x, y]


def compare_maps(map1, map2):
    same = True
    for k in range(len(map1)):
        if map1[k] != map2[k]:
            same = False
            break
    return same


def print_map(a_map):
    for x in range(len(a_map)):
        str_x = str(x)
        if x < 10:
            str_x = f'00{x}'
        elif x < 100:
            str_x = f'0{x}'
        print(f'{str_x}: {a_map[x]}')


def set_point(a_map, x, y, char):
    a_map[y] = a_map[y][:x] + char + a_map[y][x+1:]


if __name__ == "__main__":
    main()
