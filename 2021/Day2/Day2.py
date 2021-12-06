import argparse
import sys
import re
import os, os.path

def main():
    f = open("input2.txt", "r")
    input = f.read().split('\n')
    depth = 0
    length = 0

    for line in input:
        if len(line) > 1:
            dir, n = line.split(' ')
            if dir == 'forward':
                length += int(n)
            if dir == 'down':
                depth += int(n)
            if dir == 'up':
                depth -= int(n)
    print(f'Depth: {depth}, length: {length}, mult: {depth*length}')

    depth = 0
    length = 0
    aim = 0

    for line in input:
        if len(line) > 1:
            dir, n = line.split(' ')
            if dir == 'forward':
                length += int(n)
                depth += int(n)*aim
            if dir == 'down':
                aim += int(n)
            if dir == 'up':
                aim -= int(n)
    print(f'Depth: {depth}, length: {length}, mult: {depth*length}')




if __name__ == "__main__":
    main()