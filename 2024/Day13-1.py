import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input13.txt", "r")
    text = f.read()
    parts = text.split('\n\n')
    the_sum = 0

    for part in parts:
        part = part.split('\n')
        best_a = -1
        best_b = -1
        a = None
        b = None
        prize = None
        for line in part:
            if 'Button A' in line:
                bits = line.split('+')
                a = [int(bits[1].split(',')[0]), int(bits[2])]
            if 'Button B' in line:
                bits = line.split('+')
                b = [int(bits[1].split(',')[0]), int(bits[2])]
            if 'Prize' in line:
                bits = line.split('=')
                prize = [int(bits[1].split(',')[0]), int(bits[2])]

        if a and b and prize:
            for x in range(100):
                rest_x = prize[0] - x*a[0]
                rest_y = prize[1] - x*a[1]
                if rest_x % b[0] == 0 and rest_y % b[1] == 0:
                    if int(rest_x/b[0]) == int(rest_y/b[1]):
                        y = int(rest_x/b[0])
                        if 3 * x + y < 3 * best_a + best_b or best_a < 0:
                            best_a = x
                            best_b = y

        if best_a >= 0:
            t = best_a * 3 + best_b
            print(t)
            the_sum += t

    print(f'Sum: {the_sum}')


if __name__ == "__main__":
    main()
