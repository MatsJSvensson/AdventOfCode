import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input12.txt", "r")
    text = f.read()
    the_map = text.split('\n')
    the_sum = 0
    the_sum2 = 0
    width = len(the_map[0])
    height = len(the_map)
    used = []

    for y in range(height):
        for x in range(width):
            corners = []
            result = recurse(x, y, the_map[y][x], the_map, used, corners)
            the_sum += result[0] * result[1]
            n_corners = len(corners)
            the_sum2 += result[0] * n_corners

    print(f'Sum: {the_sum}')
    print(f'Sum2: {the_sum2}')


def recurse(x, y, crop, the_map, used, corners):
    width = len(the_map[0])
    height = len(the_map)
    if x < 0 or y < 0 or x > width - 1 or y > height - 1:
        return [0, 1]
    if crop != the_map[y][x]:
        return [0, 1]
    if f'{x}_{y}' in used:
        return [0, 0]

    used.append(f'{x}_{y}')
    result = []
    result.append(recurse(x, y+1, crop, the_map, used, corners))
    result.append(recurse(x, y-1, crop, the_map, used, corners))
    result.append(recurse(x+1, y, crop, the_map, used, corners))
    result.append(recurse(x-1, y, crop, the_map, used, corners))

    area = 1
    fence = 0
    for res in result:
        fence += res[1]
        area += res[0]

    new_corners = check_corners(x, y, crop, the_map)
    if len(new_corners) > 0:
        corners.extend(new_corners)
    return [area, fence]


def check_corners(x, y, crop, the_map):
    corners = []
    p1 = check_point(x - 1, y - 1, crop, the_map)
    p2 = check_point(x, y - 1, crop, the_map)
    p3 = check_point(x + 1, y - 1, crop, the_map)
    p4 = check_point(x - 1, y, crop, the_map)
    p6 = check_point(x + 1, y, crop, the_map)
    p7 = check_point(x - 1, y + 1, crop, the_map)
    p8 = check_point(x, y + 1, crop, the_map)
    p9 = check_point(x + 1, y + 1, crop, the_map)

    c1 = f'{x}_{y}'
    c2 = f'{x+1}_{y}'
    c3 = f'{x}_{y+1}'
    c4 = f'{x+1}_{y+1}'
    if not (p2 or p4):
        corners.append(c1)
    elif p2 and p4 and not p1:
        corners.append(c1)

    if not (p2 or p6):
        corners.append(c2)
    elif p2 and p6 and not p3:
        corners.append(c2)

    if not (p4 or p8):
        corners.append(c3)
    elif p4 and p8 and not p7:
        corners.append(c3)

    if not (p6 or p8):
        corners.append(c4)
    elif p6 and p8 and not p9:
        corners.append(c4)

    return corners


def check_point(x, y, crop, the_map):
    width = len(the_map[0])
    height = len(the_map)
    if x < 0 or y < 0 or x > width - 1 or y > height - 1:
        return False
    if crop != the_map[y][x]:
        return False
    return True


if __name__ == "__main__":
    main()
