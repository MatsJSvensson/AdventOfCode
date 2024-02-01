import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input12.txt", "r")
    text = f.read()
    lines = text.split('\n')
    the_sum = 0

    for line in lines:
        parts, groups = line.split(' ')
        groups = groups.split(',')

        possibilities = find_possibilities(groups, parts)

        print(possibilities)
        the_sum += possibilities

    print(the_sum)

    for x in range(len(lines)):
        line = lines[x]
        parts1, groups = line.split(' ')
        parts5 = parts1 + '?' + parts1 + '?' + parts1 + '?' + parts1 + '?' + parts1
        groups1 = groups.split(',')
        groups5 = groups1*5

        possibilities = find_possibilities(groups5, parts5)

        print(f'{x} {possibilities}')
        the_sum += possibilities

    print(the_sum)


def find_possibilities(groups, line):
    count = 0
    group = int(groups[0])
    for x in range(len(line)-group+1):
        valid = True
        if line[:x].count('#') > 0:
            break
        if len(line) > x+group and line[x+group] == '#':
            valid = False
        for y in range(x, x + group):
            if line[y] not in '#?':
                valid = False
                break
        if valid:
            if len(groups) == 1:
                if line[x+group:].count('#') == 0:
                    count += 1
            else:
                count += find_possibilities(groups[1:], line[x+group+1:])
    return count


def print_map(a_map):
    for x in range(len(a_map)):
        str_x = str(x)
        if x < 10:
            str_x = f'00{x}'
        elif x < 100:
            str_x = f'0{x}'
        print(f'{str_x}: {a_map[x]}')


if __name__ == "__main__":
    main()
