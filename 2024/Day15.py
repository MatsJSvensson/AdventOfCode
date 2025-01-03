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
        new_map.append(new_row)

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

    print_map(new_map)
    print('\n')
    new_width = len(new_map[0])
    new_height = len(new_map)

    for y in range(new_height):
        for x in range(new_width):
            if new_map[y][x] == '[':
                the_sum += x + 100 * y

    print(f'Sum: {the_sum}')


def move(pos, step, a_map, char):
    x = pos[0] + step[0]
    y = pos[1] + step[1]
    char2 = a_map[y][x]

    if char2 == '.':
        set_point(a_map, x, y, char)
        set_point(a_map, pos[0], pos[1], '.')
        return [x, y]
    if char2 == '#':
        return pos
    if char2 == '[':
        if step[1] == 0:
            move([x, y], step, a_map, char2)
            if a_map[y][x] == '.':
                set_point(a_map, x, y, char)
                set_point(a_map, pos[0], pos[1], '.')
                return [x, y]
            else:
                return pos
        else:
            if can_move([x,y], step, a_map) and can_move([x+1,y], step, a_map):
                move([x, y], step, a_map, '[')
                move([x+1, y], step, a_map, ']')
                set_point(a_map, x, y, char)
                set_point(a_map, pos[0], pos[1], '.')
                return [x, y]
            else:
                return pos
    if char2 == ']':
        if step[1] == 0:
            move([x, y], step, a_map, char2)
            if a_map[y][x] == '.':
                set_point(a_map, x, y, char)
                set_point(a_map, pos[0], pos[1], '.')
                return [x, y]
            else:
                return pos
        else:
            if can_move([x,y], step, a_map) and can_move([x-1,y], step, a_map):
                move([x-1, y], step, a_map, '[')
                move([x, y], step, a_map, ']')
                set_point(a_map, x, y, char)
                set_point(a_map, pos[0], pos[1], '.')
                return [x, y]
            else:
                return pos


def can_move(pos, step, a_map):
    x = pos[0] + step[0]
    y = pos[1] + step[1]

    if a_map[y][x] == '.':
        return True
    if a_map[y][x] == '#':
        return False
    if a_map[y][x] in '[]':
        if a_map[y][x] == '[':
            left = can_move([x, y], step, a_map)
            right = can_move([x+1, y], step, a_map)
        else:
            left = can_move([x-1, y], step, a_map)
            right = can_move([x, y], step, a_map)
        return left and right


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
