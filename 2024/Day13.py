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
                prize = [int(bits[1].split(',')[0]) + 10000000000000, int(bits[2]) + 10000000000000]

        if a and b and prize:
            if (a[0] % b[0] == 0 and a[1] % b[1] == 0) or (b[0] % a[0] == 0 and b[1] % a[1] == 0):
                if prize[0] % b[0] == 0 and prize[1] % b[1] == 0:
                    if prize[0] / b[0] == prize[1] / b[1]:
                        best_a = 0
                        best_b = prize[0] / b[0]
                elif prize[0] % b[0] == 0 and prize[1] % b[1] == 0:
                    if prize[0] / a[0] == prize[1] / a[1]:
                        best_a = prize[0] / a[0]
                        best_b = 0
            if best_a == -1:
                temp_b = (prize[0] - (a[0]/a[1]) * prize[1]) / (b[0] - (a[0]/a[1]) * b[1])
                temp_a = (prize[0] - b[0] * temp_b) / a[0]
                if my_is_integer(temp_a) and my_is_integer(temp_b):
                    best_a = temp_a
                    best_b = temp_b

        if best_a >= 0:
            t = best_a*3 + best_b
            print(t)
            the_sum += t

    print(f'Sum: {the_sum}')


def my_is_integer(num):
    s = str(num)
    if '.000' in s or '.999' in s or float.is_integer(num):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
