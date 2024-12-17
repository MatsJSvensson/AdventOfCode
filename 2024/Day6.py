import argparse
import sys
import re
import os, os.path


def main():
    f = open("input6.txt", "r")
    text = f.read()
    org_map = text.split('\n')
    width = len(org_map[0])
    height = len(org_map)
    start_pos = [-1, -1]
    dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    d = 0
    the_sum = 0

    for y in range(height):
        for x in range(width):
            if org_map[y][x] == '^':
                start_pos = [x, y]
    print(start_pos)

    too_small = False

    for y in range(height):
        print(y)
        for x in range(width):
            if org_map[y][x] in '#^':
                continue
            pos = start_pos
            d = 0
            the_map = org_map.copy()
            set_point(the_map, x, y, '*')
            done = False
            loop = False
            for t in range(100000):
                new_pos = [pos[0] + dirs[d][0], pos[1] + dirs[d][1]]
                if new_pos[0] < 0 or new_pos[0] == height or new_pos[1] < 0 or new_pos[1] == width:
                    done = True
                    break
                if the_map[new_pos[1]][new_pos[0]] in '#*':
                    d = (d + 1) % 4
                else:
                    pos = new_pos
                    if the_map[new_pos[1]][new_pos[0]] in '.^':
                        set_point(the_map, new_pos[0], new_pos[1], '0')
                    else:
                        temp = int(the_map[new_pos[1]][new_pos[0]])
                        temp += 1
                        if temp >= 4:
                            loop = True
                            break
                        set_point(the_map, new_pos[0], new_pos[1], f'{temp}')

            if loop:
                the_sum += 1
                print_map(the_map)
                print(' ')
            elif not done:
                too_small = True

    print(f'Sum: {the_sum}, too small: {too_small}')


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
