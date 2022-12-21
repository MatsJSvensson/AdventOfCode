import argparse
import sys
import re
import os, os.path
import math

f = open("input17.txt", "r")
winds = f.read()


def main():
    length = len(winds)
    counter = 0
    y_max = -1
    empty_line = '.......'
    field = [empty_line] * 8
    print(field)
    cycle = length*5
    old_cycle = 0

    for n in range(cycle*50+1):
        if n % cycle == 0:
            cycle_diff = y_max + 1 - old_cycle
            old_cycle = y_max + 1
            print(f'{y_max + 1} {cycle_diff}')

        shape = new_shape(2, y_max + 4, n % 5)
        stopped = False
        while not stopped:
            wind = winds[counter % length]
            counter += 1
            shape = gust(shape, wind, field)
            shape, stopped = fall(shape, field)
            if stopped:
                for part in shape:
                    set_point(field, part[0], part[1], '#')
                y_max = max(max([part[1] for part in shape]), y_max)
                for m in range(y_max - len(field) + 8):
                    field.append(empty_line)
                #  print_field(field)

    print(y_max+1)
    print(length)


def fall(shape, field):
    blocked = False
    other_shape = []
    for part in shape:
        x = part[0]
        y = part[1]
        if y != 0:
            if field[y - 1][x] != '.':
                blocked = True
                break
        else:
            blocked = True
            break
        other_shape.append([x, y - 1])
    if blocked:
        return shape, blocked
    else:
        return other_shape, blocked


def print_field(field):
    print('')
    for n in range(len(field)-1, -1, -1):
        print(field[n])


def gust(shape, wind, field):
    blocked = False
    direction = 1
    other_shape = []
    if wind == '<':
        direction = -1
    elif wind != '>':
        print('Bad input')
    for part in shape:
        x = part[0]
        y = part[1]
        if 0 <= x + direction <= 6:
            if field[y][x + direction] != '.':
                blocked = True
                break
        else:
            blocked = True
            break
        other_shape.append([x + direction, y])
    if blocked:
        return shape
    else:
        return other_shape


def new_shape(x, y, version):
    points = []
    if version == 0:
        points = [[x, y], [x + 1, y], [x + 2, y], [x + 3, y]]
    elif version == 1:
        points = [[x, y + 1], [x + 1, y], [x + 1, y + 1], [x + 2, y + 1], [x + 1, y + 2]]
    elif version == 2:
        points = [[x, y], [x + 1, y], [x + 2, y], [x + 2, y + 1], [x + 2, y + 2]]
    elif version == 3:
        points = [[x, y], [x, y + 1], [x, y + 2], [x, y + 3]]
    elif version == 4:
        points = [[x, y], [x + 1, y], [x + 1, y + 1], [x, y + 1]]
    else:
        print('Bad input')
        exit(1)
    return points


def set_point(cave, x, y, char):
    cave[y] = cave[y][:x] + char + cave[y][x+1:]


if __name__ == "__main__":
    main()
