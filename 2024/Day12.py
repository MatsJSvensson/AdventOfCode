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
    width = len(the_map[0])
    height = len(the_map)
    used = {}
    sum2 = 0

    for y in range(height):
        for x in range(width):
            edges = {}
            result = recurse(x, y, the_map[y][x], the_map, used, edges)
            the_sum += result[0] * result[1]
            if result[0] != 0:
                s = count_edges(f'{x}_{y}', f'{x}_{y+1}', edges)
                if s % 2 == 1:
                    s += 1
                sum2 += result[0] * s

    print(f'Sum: {the_sum}')
    print(f'Sum2: {sum2}')

    side_dict = used.copy()
    used = {}
    the_sum = 0

    for y in range(height):
        for x in range(width):
            result = recurse2(x, y, the_map[y][x], the_map, used, side_dict)
            the_sum += result[0] * result[1]

    print(f'Sum: {the_sum}')


def recurse(x, y, crop, the_map, used, edges):
    width = len(the_map[0])
    height = len(the_map)
    if x < 0 or y < 0 or x > width - 1 or y > height - 1:
        return [0, -1, '']
    if crop != the_map[y][x]:
        return [0, -1, '']
    if f'{x}_{y}' in used.keys():
        return [0, 0, used[f'{x}_{y}']]

    used[f'{x}_{y}'] = ''
    result = []
    result.append(recurse(x, y-1, crop, the_map, used, edges))
    result.append(recurse(x, y+1, crop, the_map, used, edges))
    result.append(recurse(x-1, y, crop, the_map, used, edges))
    result.append(recurse(x+1, y, crop, the_map, used, edges))

    area = 1
    fence = 0
    sides = ''
    for t in range(len(result)):
        if result[t][1] == -1:
            if t < 2:
                if str(t) not in result[2][2] and str(t) not in result[3][2]:
                    fence += 1
            else:
                if str(t) not in result[0][2] and str(t) not in result[1][2]:
                    fence += 1
            sides += str(t)
            if t == 0:
                point1 = f'{x}_{y}'
                point2 = f'{x+1}_{y}'
            elif t == 1:
                point1 = f'{x}_{y+1}'
                point2 = f'{x+1}_{y+1}'
            elif t == 2:
                point1 = f'{x}_{y}'
                point2 = f'{x}_{y+1}'
            else:
                point1 = f'{x+1}_{y}'
                point2 = f'{x+1}_{y+1}'
            if point1 in edges.keys():
                edges[point1].append(point2)
            else:
                edges[point1] = [point2]
            if point2 in edges.keys():
                edges[point2].append(point1)
            else:
                edges[point2] = [point1]

        else:
            fence += result[t][1]
        area += result[t][0]
    used[f'{x}_{y}'] = sides

    return [area, fence, sides]


def recurse2(x, y, crop, the_map, used, side_dict):
    width = len(the_map[0])
    height = len(the_map)
    if x < 0 or y < 0 or x > width - 1 or y > height - 1:
        return [0, -1, '']
    if crop != the_map[y][x]:
        return [0, -1, '']
    if f'{x}_{y}' in used.keys():
        return [0, 0, side_dict[f'{x}_{y}']]

    used[f'{x}_{y}'] = ''
    result = []
    result.append(recurse2(x, y-1, crop, the_map, used, side_dict))
    result.append(recurse2(x, y+1, crop, the_map, used, side_dict))
    result.append(recurse2(x-1, y, crop, the_map, used, side_dict))
    result.append(recurse2(x+1, y, crop, the_map, used, side_dict))

    area = 1
    fence = 0
    sides = ''
    for t in range(len(result)):
        if result[t][1] == -1:
            if t < 2:
                if str(t) not in result[2][2] and str(t) not in result[3][2]:
                    fence += 1
            else:
                if str(t) not in result[0][2] and str(t) not in result[1][2]:
                    fence += 1
            sides += str(t)
        else:
            fence += result[t][1]
        area += result[t][0]
    used[f'{x}_{y}'] = sides

    return [area, fence, sides]


def count_edges(point1, point2, edges):
    edges[point1].remove(point2)
    edges[point2].remove(point1)
    if len(edges[point1]) == 0:
        return 0
    p2 = point1
    p1 = edges[point1][0]
    x1, y1 = point2.split('_')
    x2, y2 = p1.split('_')
    res = 0
    if x1 != x2 and y1 != y2:
        res = 1
    return res + count_edges(p1, p2, edges)


if __name__ == "__main__":
    main()
