import argparse
import sys
import re
import os, os.path
import math

def main():
    f = open("input13.txt", "r")
    lines, instructions = f.read().split('\n\n')
    points = lines.split('\n')
    instructions = instructions.split('\n')

    for instruction in instructions:
        if len(instruction) > 1:
            fold = instruction.split(' ')[2]
            direction, fold_val = fold.split('=')
            fold_val = int(fold_val)

            new_points = []
            for point_str in points:
                if len(point_str) > 1:
                    point = point_str.split(',')
                    if direction == 'x':
                        x = int(point[0])
                        if x > fold_val:
                            new_x = fold_val - (x - fold_val)
                            new_str = str(new_x) + f',{point[1]}'
                        else:
                            new_str = point_str
                        if new_str not in new_points:
                            new_points.append(new_str)
                    elif direction == 'y':
                        y = int(point[1])
                        if y > fold_val:
                            new_y = fold_val - (y - fold_val)
                            new_str = f'{point[0]},' + str(new_y)
                        else:
                            new_str = point_str
                        if new_str not in new_points:
                            new_points.append(new_str)
            points = new_points

            print(len(new_points))
    max_x = 0
    max_y = 0
    for point in points:
        x, y = point.split(',')
        x = int(x)
        y = int(y)
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    code = []
    for j in range(max_y+1):
        new_row = []
        for i in range(max_x+1):
            new_row += '.'
        code.append(new_row)

    for point in points:
        x, y = point.split(',')
        x = int(x)
        y = int(y)
        code[y][x] = '#'

    for row in code:
        print(row)


if __name__ == "__main__":
    main()