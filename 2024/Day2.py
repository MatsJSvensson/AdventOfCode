import argparse
import sys
import re
import os, os.path


def main():
    f = open("input2.txt", "r")
    text = f.read()
    input = text.split('\n')
    sum = 0
    sum2 = 0

    for line in input:
        valid = True
        levels = line.split(' ')
        sign = '+'
        if int(levels[0]) > int(levels[1]):
            sign = '-'
        for n in range(len(levels)-1):
            if (int(levels[n]) > int(levels[n+1]) and sign == '+') or (int(levels[n]) < int(levels[n+1]) and sign == '-'):
                print(sign)
                valid = False
                break
            diff = abs(int(levels[n]) - int(levels[n+1]))
            if diff > 3 or diff < 1:
                print(diff)
                valid = False
                break

        if valid:
            sum += 1
        else:
            sum2 += 1

    print(f'sum: {sum} {sum2}')

    sum = 0
    sum2 = 0

    for line in input:
        valid = False
        origin = line.split(' ')
        for n in range(len(origin)):
            levels = origin.copy()
            levels.pop(n)
            valid = True
            sign = '+'
            if int(levels[0]) > int(levels[1]):
                sign = '-'
            for n in range(len(levels) - 1):
                if (int(levels[n]) > int(levels[n + 1]) and sign == '+') or (
                        int(levels[n]) < int(levels[n + 1]) and sign == '-'):
                    print(sign)
                    valid = False
                    break
                diff = abs(int(levels[n]) - int(levels[n + 1]))
                if diff > 3 or diff < 1:
                    print(diff)
                    valid = False
                    break
            if valid:
                break

        if valid:
            sum += 1
        else:
            sum2 += 1

    print(f'sum: {sum} {sum2}')


if __name__ == "__main__":
    main()
