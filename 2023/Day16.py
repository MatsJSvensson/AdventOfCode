import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input16.txt", "r")
    text = f.read()
    the_map = text.split('\n')
    energized = the_map.copy()
    follow_light(0, 0, 'r', the_map, energized)

    the_sum = 0
    for line in energized:
        for char in line:
            if char in 'hv2':
                the_sum +=1
    print(the_sum)


def follow_light(x, y, dir, the_map, energized):
    char = the_map[y][x]
    energy = energized[y][x]

    if energy in 'hv2':
        if dir in 'lr':
            if energy in 'h2':
                return
            else:
                set_point(energized, x, y, '2')
        if dir in 'ud':
            if energy in 'v2':
                return
            else:
                set_point(energized, x, y, '2')
    else:
        if dir in 'lr':
            set_point(energized, x, y, 'h')
        else:
            set_point(energized, x, y, 'v')

    new_dir = dir
    if char == '\\':
        if dir == 'r':
            new_dir = 'd'
        elif dir == 'u':
            new_dir = 'l'
        elif dir == 'l':
            new_dir = 'u'
        elif dir == 'd':
            new_dir = 'r'
    elif char == '/':
        if dir == 'r':
            new_dir = 'u'
        elif dir == 'u':
            new_dir = 'r'
        elif dir == 'l':
            new_dir = 'd'
        elif dir == 'd':
            new_dir = 'l'
    elif char == '|':
        if dir in 'rl':
            new_dir = 'v'
    elif char == '-':
        if dir in 'ud':
            new_dir = 'h'

    if new_dir in 'hl' and x > 0:
        follow_light(x-1, y, 'l', the_map, energized)
    if new_dir in 'hr' and x < len(the_map[0])-1:
        follow_light(x+1, y, 'r', the_map, energized)
    if new_dir in 'vu' and y > 0:
        follow_light(x, y-1, 'u', the_map, energized)
    if new_dir in 'vd' and y < len(the_map)-1:
        follow_light(x, y+1, 'd', the_map, energized)


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
