import argparse
import sys
import re
import os, os.path
import math
import aoc_utils as utils

def main():
    f = open("input16.txt", "r")
    text = f.read()
    the_map = text.split('\n')
    width = len(the_map[0])
    height = len(the_map)

    x0 = -1
    y0 = -1
    x9 = -1
    y9 = -1

    score_map = {}

    for y in range(height):
        for x in range(width):
            if the_map[y][x] == 'S':
                x0 = x
                y0 = y
            if the_map[y][x] == 'E':
                x9 = x
                y9 = y

    sys.setrecursionlimit(100000)
    go(x0, y0, [1, 0], the_map, score_map, 0)

    name = f'{x9}_{y9}'
    target = score_map[name][1]
    for y in range(height):
        for x in range(width):
            name = f'{x}_{y}'
            if name in score_map.keys():
                if score_map[name][1] == target:
                    utils.set_point(the_map, x, y, 'O')
    utils.print_map(the_map)

    name = f'{x9}_{y9}'
    print(f'Sum: {score_map[name][0]}')

    the_sum = 0
    for key in score_map.keys():
        if score_map[key][1] == target:
            the_sum += 1

    print(f'Sum: {the_sum}')


def go(x, y, dir, the_map, score_map, score):
    char = the_map[y][x]
    if char == '.' or char == 'S':
        name = f'{x}_{y}'
        if name in score_map.keys():
            if score < score_map[name][0]:
                score_map[name] = [score, 0]
            elif score == score_map[name][0] and score_map[name][1] > 0:
                return score_map[name][1]
            else:
                return 0
        else:
            score_map[name] = [score, 0]

        part_of_path = go(x + dir[0], y + dir[1], dir, the_map, score_map, score + 1)
        score += 1000
        temp = go(x + dir[1], y + dir[0], [dir[1], dir[0]], the_map, score_map, score + 1)
        if 0 < temp:
            if part_of_path > 0:
                if temp < part_of_path:
                    part_of_path = temp
                    score_map[name][0] = score
            else:
                part_of_path = temp
                score_map[name][0] = score
        temp = go(x - dir[1], y - dir[0], [-dir[1], -dir[0]], the_map, score_map, score + 1)
        if 0 < temp:
            if part_of_path > 0:
                if temp < part_of_path:
                    part_of_path = temp
                    score_map[name][0] = score
            else:
                part_of_path = temp
                score_map[name][0] = score
        if part_of_path > 0: # More?
            score_map[name][1] = part_of_path
        return part_of_path
    elif char == 'E':
        name = f'{x}_{y}'
        if name in score_map.keys():
            if score < score_map[name][0]:
                score_map[name] = [score, score]
                return score
            elif score == score_map[name][0]:
                return score
            else:
                return 0
        else:
            score_map[name] = [score, score]
            return score
    else:
        return 0


if __name__ == "__main__":
    main()
