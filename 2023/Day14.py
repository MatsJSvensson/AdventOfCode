import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input14.txt", "r")
    text = f.read()
    org_map = text.split('\n')
    the_map = org_map.copy()
    the_sum = 0
    for x in range(len(the_map[0])):
        stop = -1
        for y in range(len(the_map)):
            if the_map[y][x] == '#':
                stop = y
            elif the_map[y][x] == 'O':
                set_point(the_map, x, y, '.')
                set_point(the_map, x, stop + 1, 'O')
                stop += 1

    print_map(the_map)

    for x in range(len(the_map[0])):
        for y in range(len(the_map)):
            if the_map[y][x] == 'O':
                the_sum += len(the_map) - y

    print(the_sum)

    the_map = org_map.copy()
    map_list = []
    cycle = -1
    for i in range(500):
        new_map = the_map.copy()
        north(new_map)
        west(new_map)
        south(new_map)
        east(new_map)

        if i >= 200:
            add = True
            for k in range(len(map_list)):
                if compare_maps(new_map, map_list[k]):
                    add = False
            if add:
                map_list.append(new_map)
            else:
                print(f'cycle: {len(map_list)}')
                cycle = len(map_list)
                print(f'Done at {i}!')
                break

        # same = True
        # for k in range(len(the_map)):
        #     if new_map[k] != the_map[k]:
        #         print(i)
        #         print(f'{k} {the_map[k]}')
        #         print(f'{k} {new_map[k]}')
        #         same = False
        #         break
        # if same:
        #     print(f'Done at {i}!')
        #     break
        # else:
        the_map = new_map

    rest1 = 1000000000 % cycle
    rest2 = 200 % cycle
    rest = rest1 - rest2 - 1

    the_sum = 0
    sums = []
    for i in range(len(map_list)):
        a_sum = 0
        for x in range(len(the_map[0])):
            for y in range(len(the_map)):
                if map_list[i][y][x] == 'O':
                    a_sum += len(the_map) - y
        sums.append(a_sum)

    print(sums)
    # 96132 too high
    # 96096 too low


def compare_maps(map1, map2):
    same = True
    for k in range(len(map1)):
        if map1[k] != map2[k]:
            #print(i)
            #print(f'{k} {the_map[k]}')
            #print(f'{k} {new_map[k]}')
            same = False
            break
    return same


def north(the_map):
    for x in range(len(the_map[0])):
        stop = -1
        for y in range(len(the_map)):
            if the_map[y][x] == '#':
                stop = y
            elif the_map[y][x] == 'O':
                set_point(the_map, x, y, '.')
                set_point(the_map, x, stop + 1, 'O')
                stop += 1


def south(the_map):
    for x in range(len(the_map[0])):
        stop = len(the_map)
        for y in range(len(the_map)-1, -1, -1):
            if the_map[y][x] == '#':
                stop = y
            elif the_map[y][x] == 'O':
                set_point(the_map, x, y, '.')
                set_point(the_map, x, stop - 1, 'O')
                stop -= 1


def east(the_map):
    for y in range(len(the_map)):
        stop = len(the_map[0])
        for x in range(len(the_map[0])-1, -1, -1):
            if the_map[y][x] == '#':
                stop = x
            elif the_map[y][x] == 'O':
                set_point(the_map, x, y, '.')
                set_point(the_map, stop - 1, y, 'O')
                stop -= 1


def west(the_map):
    for y in range(len(the_map)):
        stop = -1
        for x in range(len(the_map[0])):
            if the_map[y][x] == '#':
                stop = x
            elif the_map[y][x] == 'O':
                set_point(the_map, x, y, '.')
                set_point(the_map, stop + 1, y, 'O')
                stop += 1


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
