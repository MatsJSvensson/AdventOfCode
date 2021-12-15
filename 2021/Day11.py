import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input11.txt", "r")
    lines = f.readlines()

    rows = []

    for line in lines:
        temp_list = []
        if len(line) > 1:
            for char in line.strip():
                temp_list.append(int(char))
            rows.append(temp_list)

    height = len(rows)
    width = len(rows[0])
    flash_sum = 0

    for i in range(500):
        for y in range(height):
            for x in range(width):
                rows[y][x] += 1
        new_rows = []
        for row in rows:
            new_rows.append(row.copy())

        flashed = True
        while flashed:
            flashed = False
            for y in range(height):
                for x in range(width):
                    if rows[y][x] > 9 and new_rows[y][x] != 0:
                        flash_sum += 1
                        new_rows[y][x] = 0
                        flashed = True

                        for k in range(max(0,y-1),min(height,y+2)):
                            for j in range(max(0,x-1),min(width,x+2)):
                                rows[k][j] += 1

        nFlashed = 0
        for y in range(height):
            for x in range(width):
                if new_rows[y][x] != 0:
                    new_rows[y][x] = rows[y][x]
                else:
                    nFlashed += 1
        rows = new_rows
        for row in rows:
            print(row)
        print('\n')
        if nFlashed == height * width:
            print(i)
            break

    print(f'sum = {flash_sum}')


if __name__ == "__main__":
    main()