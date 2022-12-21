import argparse
import sys
import re
import os, os.path
import math


def set_point(a_map, x, y, z, char):
    a_map[z][y] = a_map[z][y][:x] + char + a_map[z][y][x+1:]


f = open("input19.txt", "r")
text = f.read()
lines = text.split('\n')
blueprints = {}
for line in lines:
    blueprint_id = line.split(':')[0].split(' ')[1]
    parts = line.split('robot costs ')
    ore = parts[1].split('.')[0]
    clay = parts[2].split('.')[0]
    obsidian = parts[3].split('.')[0]
    geode = parts[4]. split('.')[0]


def main():
    a_sum = 0
    for zz in range(len(map_3D)-1):
        for yy in range(len(map_3D[zz])-1):
            for xx in range(len(map_3D[zz][yy])-1):
                if map_3D[zz][yy][xx] == '#':
                    if zz != 0:
                        if map_3D[zz-1][yy][xx] == '.':
                            a_sum += 1
                    else:
                        a_sum += 1
                    if yy != 0:
                        if map_3D[zz][yy-1][xx] == '.':
                            a_sum += 1
                    else:
                        a_sum += 1
                    if xx != 0:
                        if map_3D[zz][yy][xx-1] == '.':
                            a_sum += 1
                    else:
                        a_sum += 1
                    if map_3D[zz][yy][xx+1] == '.':
                        a_sum += 1
                    if map_3D[zz][yy+1][xx] == '.':
                        a_sum += 1
                    if map_3D[zz+1][yy][xx] == '.':
                        a_sum += 1
    print(a_sum)
    for n in range(max_range*2):
        for zz in range(len(map_3D)):
            for yy in range(len(map_3D[zz])):
                for xx in range(len(map_3D[zz][yy])):
                    if map_3D[zz][yy][xx] == '.':
                        if zz == 0:
                            set_point(map_3D, xx, yy, zz, '-')
                        elif map_3D[zz-1][yy][xx] == '-':
                            set_point(map_3D, xx, yy, zz, '-')
                        elif yy == 0:
                            set_point(map_3D, xx, yy, zz, '-')
                        elif map_3D[zz][yy-1][xx] == '-':
                            set_point(map_3D, xx, yy, zz, '-')
                        elif xx == 0:
                            set_point(map_3D, xx, yy, zz, '-')
                        elif map_3D[zz][yy][xx-1] == '-':
                            set_point(map_3D, xx, yy, zz, '-')
                        elif xx == max_range-1:
                            set_point(map_3D, xx, yy, zz, '-')
                        elif map_3D[zz][yy][xx+1] == '-':
                            set_point(map_3D, xx, yy, zz, '-')
                        elif yy == max_range-1:
                            set_point(map_3D, xx, yy, zz, '-')
                        elif map_3D[zz][yy+1][xx] == '-':
                            set_point(map_3D, xx, yy, zz, '-')
                        elif zz == max_range-1:
                            set_point(map_3D, xx, yy, zz, '-')
                        elif map_3D[zz+1][yy][xx] == '-':
                            set_point(map_3D, xx, yy, zz, '-')

    a_sum = 0
    for zz in range(len(map_3D) - 1):
        for yy in range(len(map_3D[zz]) - 1):
            for xx in range(len(map_3D[zz][yy]) - 1):
                if map_3D[zz][yy][xx] == '#':
                    if zz != 0:
                        if map_3D[zz - 1][yy][xx] == '-':
                            a_sum += 1
                    else:
                        a_sum += 1
                    if yy != 0:
                        if map_3D[zz][yy - 1][xx] == '-':
                            a_sum += 1
                    else:
                        a_sum += 1
                    if xx != 0:
                        if map_3D[zz][yy][xx - 1] == '-':
                            a_sum += 1
                    else:
                        a_sum += 1
                    if map_3D[zz][yy][xx + 1] == '-':
                        a_sum += 1
                    if map_3D[zz][yy + 1][xx] == '-':
                        a_sum += 1
                    if map_3D[zz + 1][yy][xx] == '-':
                        a_sum += 1
    print(a_sum)


if __name__ == "__main__":
    main()
