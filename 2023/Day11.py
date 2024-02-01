import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input11.txt", "r")
    text = f.read()
    the_map = text.split('\n')
    columns = []
    rows = []

    for y in range(len(the_map)):
        if '#' not in the_map[y]:
            columns.append(y)
    for x in range(len(the_map[0])):
        double = True
        for y in range(len(the_map)):
            if the_map[y][x] == '#':
                double = False
        if double:
            rows.append(x)

    columns.reverse()
    new_map = the_map.copy()
    for y in columns:
        new_map.insert(y+1, the_map[columns[0]])

    rows.reverse()
    for x in rows:
        for y in range(len(new_map)):
            new_map[y] = new_map[y][:x+1] + '.' + new_map[y][x+1:]
    print_map(new_map)

    points = []
    for x in range(len(new_map[0])):
        for y in range(len(new_map)):
            if new_map[y][x] == '#':
                points.append([x, y])

    the_sum = 0
    for i in range(len(points)):
        for k in range(i+1, len(points)):
            distance = math.fabs(points[i][0] - points[k][0]) + math.fabs(points[i][1] - points[k][1])
            the_sum += distance

    print(the_sum)

    # Part 2
    columns = []
    rows = []

    for y in range(len(the_map)):
        if '#' not in the_map[y]:
            columns.append(y)
    for x in range(len(the_map[0])):
        double = True
        for y in range(len(the_map)):
            if the_map[y][x] == '#':
                double = False
        if double:
            rows.append(x)

    points = []
    for x in range(len(the_map[0])):
        for y in range(len(the_map)):
            if the_map[y][x] == '#':
                points.append([x, y])

    the_sum = 0
    for i in range(len(points)):
        for k in range(i+1, len(points)):
            distance = math.fabs(points[i][0] - points[k][0]) + math.fabs(points[i][1] - points[k][1])
            millions = 0
            if points[i][0] < points[k][0]:
                low_x = points[i][0]
                high_x = points[k][0]
            else:
                low_x = points[k][0]
                high_x = points[i][0]
            for x in rows:
                if low_x < x < high_x:
                    millions += 1
            if points[i][1] < points[k][1]:
                low_y = points[i][1]
                high_y = points[k][1]
            else:
                low_y = points[k][1]
                high_y = points[i][1]
            for y in columns:
                if low_y < y < high_y:
                    millions += 1
            diff = distance + millions * 999999
            the_sum += diff

    print(the_sum)


def print_map(a_map):
    for x in range(len(a_map)):
        str_x = str(x)
        if x < 10:
            str_x = f'00{x}'
        elif x < 100:
            str_x = f'0{x}'
        print(f'{str_x}: {a_map[x]}')


if __name__ == "__main__":
    main()
