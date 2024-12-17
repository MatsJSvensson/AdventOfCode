import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input14.txt", "r")
    text = f.read()
    lines = text.split('\n')
    robots = []
    width = 101
    height = 103
    a_map = '.' * width
    a_map = [a_map] * height

    for line in lines:
        parts = line.split(' ')
        pos = parts[0].split('=')[1]
        vel = parts[1].split('=')[1]
        p = pos.split(',')
        v = vel.split(',')
        robot = { 'p': [int(p[0]), int(p[1])], 'v': [int(v[0]), int(v[1])]}
        robots.append(robot)

    for t in range(width*height):
        new_map = a_map.copy()
        double = False
        for robot in robots:
            p = robot['p']
            v = robot['v']
            p[0] += v[0]
            p[1] += v[1]
            if p[0] > width - 1:
                p[0] = p[0] % width
            if p[1] > height - 1:
                p[1] = p[1] % height
            if p[0] < 0:
                p[0] += width
            if p[1] < 0:
                p[1] += height
            if not set_point(new_map, p[0], p[1], '*'):
                double = True

        if not double:
            print(f'\n{t}')
            print_map(new_map)

    quads = [0,0,0,0]
    for robot in robots:
        p = robot['p']
        if p[0] < width/2 - 1 and p[1] < height/2 - 1:
            quads[0] += 1
        if p[0] < width/2 - 1 and p[1] > height/2:
            quads[1] += 1
        if p[0] > width/2 and p[1] < height/2 - 1:
            quads[2] += 1
        if p[0] > width/2 and p[1] > height/2:
            quads[3] += 1

    the_sum = 1
    for q in quads:
        the_sum *= q

    print(f'Sum: {the_sum}')


def print_map(a_map):
    for x in range(len(a_map)):
        str_x = str(x)
        if x < 10:
            str_x = f'00{x}'
        elif x < 100:
            str_x = f'0{x}'
        print(f'{str_x}: {a_map[x]}')


def set_point(a_map, x, y, char):
    if a_map[y][x] == '*':
        return False
    a_map[y] = a_map[y][:x] + char + a_map[y][x+1:]
    return True


if __name__ == "__main__":
    main()
