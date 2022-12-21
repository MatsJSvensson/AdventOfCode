import argparse
import sys
import re
import os, os.path
import math

f = open("input14.txt", "r")
text = f.read()
lines = text.split('\n')


def main():
    segments = []
    xx = []
    yy = []
    for line in lines:
        points = line.split(' -> ')
        x, y = points[0].split(',')
        xx.append(int(x))
        yy.append(int(y))
        old_point = [int(x), int(y)]
        for point in points[1:]:
            x, y = point.split(',')
            xx.append(int(x))
            yy.append(int(y))
            new_point = [int(x), int(y)]
            segments.append([old_point, new_point])
            old_point = new_point

    max_x = max(xx)
    min_x = min(xx)
    max_y = max(yy) + 2
    min_y = min(yy)
    print(f'{min_x}, {max_x}, {min_y}, {max_y}')

    segments.append([[500-max_y, max_y], [500+max_y, max_y]])
    max_x = max([max_x, 500 + max_y])
    min_x = min([min_x, 500 - max_y])

    vertical = '.' * (max_x - min_x + 1)
    cave = [vertical] * (max_y + 1)

    for segment in segments:
        if segment[0][0] == segment[1][0]:
            x = segment[0][0] - min_x
            if segment[0][1] < segment[1][1]:
                for y in range(segment[0][1], segment[1][1] + 1):
                    set_point(cave, x, y, '#')
            else:
                for y in range(segment[1][1], segment[0][1] + 1):
                    set_point(cave, x, y, '#')
        else:
            y = segment[0][1]
            if segment[0][0] < segment[1][0]:
                for x in range(segment[0][0] - min_x, segment[1][0] + 1 - min_x):
                    set_point(cave, x, y, '#')
            else:
                for x in range(segment[1][0] - min_x, segment[0][0] + 1 - min_x):
                    set_point(cave, x, y, '#')
            #x1 = min([segment[0][0], segment[1][0]]) - min_x
            #x2 = max([segment[0][0], segment[1][0]]) - min_x
            #cave[y] = cave[y][:x1] + '#' * (abs(x2-x1)+1) + cave[y][x2+1:]

    #print_cave(cave)
    sand = 0
    set_point(cave, 500 - min_x, 0, '+')

    for n in range(50000):
        sand_x = 500 - min_x
        sand_y = 0
        lost = False
        for m in range(max_y+1):
            if sand_y == max_y:
                lost = True
                break
            if cave[sand_y+1][sand_x] == '.':
                sand_y += 1
            elif cave[sand_y+1][sand_x-1] == '.':
                sand_y += 1
                sand_x -= 1
            elif cave[sand_y + 1][sand_x + 1] == '.':
                sand_y += 1
                sand_x += 1
            else:
                if sand_y == 0:
                    lost = True
                set_point(cave, sand_x, sand_y, 'o')
        if lost:
            sand = n
            break

    print_cave(cave)
    print(sand)
    print(sum([part.count('o') for part in cave]))


def print_cave(cave):
    for n in range(len(cave)):
        print(f'{cave[n]} {n}')
    print('')


def set_point(cave, x, y, char):
    cave[y] = cave[y][:x] + char + cave[y][x+1:]


if __name__ == "__main__":
    main()
