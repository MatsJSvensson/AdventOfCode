import argparse
import sys
import re
import os, os.path
import math

f = open("input22.txt", "r")
text = f.read()
map_input, route_input = text.split('\n\n')
a_map = map_input.split('\n')
x_max = max(len(line) for line in a_map)
for n in range(len(a_map)):
    if len(a_map[n]) < x_max:
        a_map[n] += ' ' * (x_max - len(a_map[n]))
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


def main():
    dir = 0
    x = 0
    y = 0
    for n in range(len(a_map[y])):
        if a_map[y][n] == '.':
            x = n
            break
    for command in route:
        if isinstance(command, int):
            for n in range(command):
                new_x = x + dirs[dir][0]
                new_y = y + dirs[dir][1]
                if new_x < 0:
                    new_x = len(a_map[y]) - 1
                if new_x > len(a_map[y]) - 1:
                    new_x = 0
                if new_y < 0:
                    new_y = len(a_map) - 1
                if new_y > len(a_map) - 1:
                    new_y = 0
                if a_map[new_y][new_x] == ' ':
                    for m in range(len(a_map)*2):
                        new_x = new_x + dirs[dir][0]
                        new_y = new_y + dirs[dir][1]
                        if new_x < 0:
                            new_x = len(a_map[y]) - 1
                        if new_x > len(a_map[y]) - 1:
                            new_x = 0
                        if new_y < 0:
                            new_y = len(a_map) - 1
                        if new_y > len(a_map) - 1:
                            new_y = 0
                        if a_map[new_y][new_x] != ' ':
                            break
                if a_map[new_y][new_x] == '#':
                    break
                else:
                    x = new_x
                    y = new_y
        else:
            if command == 'R':
                dir = (dir + 1) % 4
            else:
                dir = (dir - 1) % 4
    print(x, y, dir)
    print((y + 1) * 1000 + (x + 1) * 4 + dir)


if __name__ == "__main__":
    main()
