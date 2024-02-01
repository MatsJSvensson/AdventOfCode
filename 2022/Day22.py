import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input22.txt", "r")
    text = f.read()
    map_input, route_input = text.split('\n\n')
    a_map = map_input.split('\n')
    side_length = 50
    sides = []
    for n in range(int(len(a_map) / side_length)):
        for m in range(int(len(a_map[n * side_length]) / side_length)):
            if a_map[n * side_length][m * side_length] != ' ':
                side = []
                for y in range(n * side_length, (n + 1) * side_length):
                    side.append(a_map[y][m * side_length:(m + 1) * side_length])
                sides.append(side)

    neighbours = [[[1, 0], [2, 1], [3, 0], [5, 0]],
                  [[4, 2], [2, 2], [0, 2], [5, 3]],
                  [[1, 3], [4, 1], [3, 1], [0, 3]],
                  [[4, 0], [5, 1], [0, 0], [2, 0]],
                  [[1, 2], [5, 2], [3, 2], [2, 3]],
                  [[4, 3], [1, 1], [0, 1], [3, 3]]]

    route = []
    number = ''
    letters = 'RL'
    for char in route_input:
        if char in letters:
            route.append(int(number))
            route.append(char)
            number = ''
        else:
            number += char
    if number != '':
        route.append(int(number))

    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    dir_char = '>v<^'

    dir = 0
    x = 0
    y = 0
    side = 0
    set_point(sides[side], x, y, dir_char[dir])
    for command in route:
        if isinstance(command, int):
            for n in range(command):
                new_x = x + dirs[dir][0]
                new_y = y + dirs[dir][1]
                new_side = side
                new_dir = dir
                if new_x < 0:
                    new_side = neighbours[side][2][0]
                    new_dir = neighbours[side][2][1]
                    if new_dir == 0:
                        new_x = 0
                        new_y = side_length - 1 - new_y
                    if new_dir == 1:
                        new_x = new_y
                        new_y = 0
                    if new_dir == 2:
                        new_x = side_length - 1
                    if new_dir == 3:
                        new_x = side_length - 1 - new_y
                        new_y = side_length - 1
                if new_x > side_length - 1:
                    new_side = neighbours[side][0][0]
                    new_dir = neighbours[side][0][1]
                    if new_dir == 0:
                        new_x = 0
                    if new_dir == 1:
                        new_x = side_length - 1 - new_y
                        new_y = 0
                    if new_dir == 2:
                        new_y = side_length - 1 - new_y
                        new_x = side_length - 1
                    if new_dir == 3:
                        new_x = new_y
                        new_y = side_length - 1
                if new_y < 0:
                    new_side = neighbours[side][3][0]
                    new_dir = neighbours[side][3][1]
                    if new_dir == 0:
                        new_y = new_x
                        new_x = 0
                    if new_dir == 1:
                        new_x = side_length - 1 - new_x
                        new_y = 0
                    if new_dir == 2:
                        new_y = side_length - 1 - new_x
                        new_x = side_length - 1
                    if new_dir == 3:
                        new_y = side_length - 1
                if new_y > side_length - 1:
                    new_side = neighbours[side][1][0]
                    new_dir = neighbours[side][1][1]
                    if new_dir == 0:
                        new_y = side_length - 1 - new_x
                        new_x = 0
                    if new_dir == 1:
                        new_y = 0
                    if new_dir == 2:
                        new_y = new_x
                        new_x = side_length - 1
                    if new_dir == 3:
                        new_x = side_length - 1 - new_x
                        new_y = side_length - 1
                if sides[new_side][new_y][new_x] == '#':
                    break
                else:
                    x = new_x
                    y = new_y
                    side = new_side
                    dir = new_dir
                    set_point(sides[side], x, y, dir_char[dir])
        else:
            if command == 'R':
                dir = (dir + 1) % 4
            else:
                dir = (dir - 1) % 4
            set_point(sides[side], x, y, dir_char[dir])
        print(command)
        print(x, y, dir, side)
        print_side(sides[side])
        pass

    print((y + 101) * 1000 + (x + 51) * 4 + dir)


def set_point(a_map, x, y, char):
    a_map[y] = a_map[y][:x] + char + a_map[y][x+1:]


def print_side(text):
    for line in text:
        print(line)
    print('')


if __name__ == "__main__":
    main()
