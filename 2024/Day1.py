import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input1.txt", "r")
    text = f.read()

    input = text.split('\n')
    list1 = []
    list2 = []

    for line in input:
        if '   ' in line:
            val1, val2 = line.split('   ')
            list1.append(int(val1))
            list2.append(int(val2))

    list1.sort()
    list2.sort()

    sum = 0
    for n in range(0, len(list1)):
        sum += abs(list1[n] - list2[n])

    print(f'sum: {sum}')

    sum = 0
    for n in range(0, len(list1)):
        sum += list1[n] * list2.count(list1[n])

    print(f'sum: {sum}')


if __name__ == "__main__":
    main()
