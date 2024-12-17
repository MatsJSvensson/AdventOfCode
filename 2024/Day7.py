import argparse
import sys
import re
import os, os.path


def main():
    f = open("input7.txt", "r")
    text = f.read()
    lines = text.split('\n')
    the_sum = 0

    for line in lines:
        goal, parts = line.split(': ')
        parts = [int(x) for x in parts.split(' ')]
        goal = int(goal)
        if test(goal, parts, parts[0], 1):
            the_sum += goal

    print(f'sum: {the_sum}')


def test(goal, parts, total, x):
    if x == len(parts):
        if goal == total:
            return True
        else:
            return False
    else:
        plus = test(goal, parts, total + parts[x], x+1)
        mult = test(goal, parts, total * parts[x], x+1)
        string = str(total) + str(parts[x])
        conc = test(goal, parts, int(string), x+1)
        return mult or plus or conc



if __name__ == "__main__":
    main()
