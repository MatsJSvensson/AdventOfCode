import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input23.txt", "r")
    text = f.read()
    a_map = text.split('\n')
    length = len(a_map)
    width = len(a_map[0])
    n_rounds = 1000
    template = '.' * (width + 2 * n_rounds)
    new_map = [template] * n_rounds
    for n in range(length):
        new_map.append('.' * n_rounds + a_map[n] + '.' * n_rounds)
    new_map.extend([template] * n_rounds)

    elves = {}
    counter = 0
    start_dir = 0
    for y in range(n_rounds, length + n_rounds):
        for x in range(n_rounds, width + n_rounds):
            if new_map[y][x] == '#':
                elves[counter] = [x, y]
                counter += 1

    # print_map(new_map)
    for n in range(n_rounds):
        new_positions = {}
        for m in range(counter):
            if check_surround(elves[m], new_map):
                new_pos = check_direction(elves[m], new_map, start_dir)
                if new_pos:
                    name = f'{new_pos[0]} {new_pos[1]}'
                    if name in new_positions.keys():
                        new_positions[name].append(m)
                    else:
                        new_positions[name] = [m]
        if len(new_positions.keys()) == 0:
            break
        start_dir = (start_dir + 1) % 4
        for key in new_positions.keys():
            if len(new_positions[key]) == 1:
                elf = new_positions[key][0]
                x = int(key.split(' ')[0])
                y = int(key.split(' ')[1])
                set_point(new_map, elves[elf][0], elves[elf][1], '.')
                set_point(new_map, x, y, '#')
                elves[elf] = [x, y]
        #print_map(new_map)
        pass
    x_min = min(elf[0] for elf in elves.values())
    x_max = max(elf[0] for elf in elves.values())
    y_max = max(elf[1] for elf in elves.values())
    y_min = min(elf[1] for elf in elves.values())
    a_sum = 0
    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            if new_map[y][x] == '.':
                a_sum += 1

    print(a_sum)
    print(n)
    print(new_positions)


def check_surround(position, a_map):
    found = False
    x = position[0]
    y = position[1]
    for a in range(x-1, x+2):
        for b in range(y-1, y+2):
            if a_map[b][a] == '#' and not (a == x and b == y):
                found = True
    return found


def check_direction(position, a_map, start):
    directions = 'NSWE'
    for n in range(4):
        char = directions[(start + n) % 4]
        if char == 'N':
            found = False
            y = position[1] - 1
            for x in range(position[0] - 1, position[0] + 2):
                if a_map[y][x] == '#':
                    found = True
            if not found:
                return [position[0], y]
        elif char == 'S':
            found = False
            y = position[1] + 1
            for x in range(position[0] - 1, position[0] + 2):
                if a_map[y][x] == '#':
                    found = True
            if not found:
                return [position[0], y]
        elif char == 'W':
            found = False
            x = position[0] - 1
            for y in range(position[1] - 1, position[1] + 2):
                if a_map[y][x] == '#':
                    found = True
            if not found:
                return [x, position[1]]
        elif char == 'E':
            found = False
            x = position[0] + 1
            for y in range(position[1] - 1, position[1] + 2):
                if a_map[y][x] == '#':
                    found = True
            if not found:
                return [x, position[1]]
    return None


def set_point(a_map, x, y, char):
    a_map[y] = a_map[y][:x] + char + a_map[y][x+1:]


def print_map(a_map):
    for line in a_map:
        print(line)
    print('')


if __name__ == "__main__":
    main()
