import argparse
import sys
import re
import os, os.path
import math

def main():
    f = open("input9.txt", "r")
    the_input = f.readlines()

    rows = []

    for row in the_input:
        if len(row) > 1:
            temp_list = []
            for char in row.strip():
                temp_list.append(int(char))
            rows.append(temp_list)

    height = len(rows)
    width = len(rows[0])
    the_sum = 0
    low_points = []

    for y in range(height):
        for x in range(width):
            low_point = True
            if x > 0:
                if rows[y][x] >= rows[y][x-1]:
                    low_point = False
            if x < width - 1:
                if rows[y][x] >= rows[y][x+1]:
                    low_point = False
            if y > 0:
                if rows[y][x] >= rows[y-1][x]:
                    low_point = False
            if y < height - 1:
                if rows[y][x] >= rows[y+1][x]:
                    low_point = False
            if low_point:
                the_sum += rows[y][x] + 1
                low_points.append(str(x) + ',' + str(y))

    basin_sizes = []
    for y in range(height):
        for x in range(width):
            if str(x) + ',' + str(y) in low_points:
                basin = []
                basin = find_basin(x, y, rows, basin)
                basin_sizes.append(len(basin))

    max = [0,0,0]
    for s in basin_sizes:
        if s > max[0]:
            max[0] = s
            if s > max[1]:
                max[0] = max[1]
                max[1] = s
                if s > max[2]:
                    max[1] = max[2]
                    max[2] = s

    the_prod = max[0] * max[1] * max[2]

    print(f'sums = {the_sum}', {the_prod})


def find_basin(x, y, the_map, basin=[]):
    basin.append(str(x) + ',' + str(y))
    if x > 0:
        if the_map[y][x-1] != 9 and str(x-1) + ',' + str(y) not in basin:
            find_basin(x-1,y,the_map,basin)
    if x < len(the_map[0]) - 1:
        if the_map[y][x+1] != 9 and str(x+1) + ',' + str(y) not in basin:
            find_basin(x+1,y,the_map,basin)
    if y > 0:
        if the_map[y-1][x] != 9 and str(x) + ',' + str(y-1) not in basin:
            find_basin(x,y-1,the_map,basin)
    if y < len(the_map) - 1:
        if the_map[y+1][x] != 9 and str(x) + ',' + str(y+1) not in basin:
            find_basin(x,y+1,the_map,basin)
    return basin


if __name__ == "__main__":
    main()