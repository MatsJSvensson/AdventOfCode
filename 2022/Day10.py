import argparse
import sys
import re
import os, os.path


def main():
    f = open("input10.txt", "r")
    lines = f.read().split('\n')

    register = 1
    cycle = 1
    cycle_map = {}

    for line in lines:
        if line != '':
            command = line.split(' ')[0]
            if command == 'noop':
                cycle_map[cycle] = register
                cycle += 1
            else:
                value = line.split(' ')[1]
                cycle_map[cycle] = register
                cycle_map[cycle+1] = register
                cycle += 2
                register += int(value)

    the_sum = 0
    for n in range(20, 221, 40):
        the_sum += n * cycle_map[n]
    print(the_sum)

    picture = ''
    cycle_map[cycle] = register

    for n in range(1, cycle + 1):
        if cycle_map[n] - 1 <= (n - 1) % 40 <= cycle_map[n] + 1:
            picture += '#'
        else:
            picture += '.'

        if n % 40 == 0:
            print(picture[n-40:n])

    pass


if __name__ == "__main__":
    main()
