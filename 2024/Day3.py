import argparse
import sys
import re
import os, os.path


def main():
    f = open("input3.txt", "r")
    text = f.read()
    input = text.split('\n')
    sum = 0

    for line in input:
        rest = line.split('mul(')
        for n in range(1, len(rest)):
            mid = rest[n].split(')')[0]
            parts = mid.split(',')
            if len(parts) == 2:
                only_num = True
                for part in parts:
                    for char in part:
                        if char not in '0123456789':
                            only_num = False
                            break
                if only_num:
                    sum += int(parts[0]) * int(parts[1])

    print(f'sum: {sum}')

    sum = 0

    for line in input:
        dos = line.split("do()")
        for don in dos:
            todo = don.split("don't()")[0]
            rest = todo.split('mul(')
            for n in range(1, len(rest)):
                mid = rest[n].split(')')[0]
                parts = mid.split(',')
                if len(parts) == 2:
                    only_num = True
                    for part in parts:
                        for char in part:
                            if char not in '0123456789':
                                only_num = False
                                break
                    if only_num:
                        sum += int(parts[0]) * int(parts[1])

    print(f'sum: {sum}')


if __name__ == "__main__":
    main()
