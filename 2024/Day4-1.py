import argparse
import sys
import re
import os, os.path


def main():
    f = open("input4.txt", "r")
    text = f.read()
    input = text.split('\n')
    width = len(input[0])
    height = len(input)
    the_sum = 0

    for n in range(height):
        for m in range(width):
            if input[n][m] == 'A':
                nFound = find_first(n, m, input)
                the_sum += nFound

    print(f'The sum = {the_sum}')


def find_first(n, m, input):
    a_sum = 0
    c1 = find_next(n-1, m-1, input)
    c2 = find_next(n+1, m+1, input)
    c3 = find_next(n-1, m+1, input)
    c4 = find_next(n+1, m-1, input)
    if c1 == 'M' and c2 == 'S' or c1 == 'S' and c2 == 'M':
        a_sum += 1
    if c3 == 'M' and c4 == 'S' or c3 == 'S' and c4 == 'M':
        a_sum += 1
    if a_sum == 2:
        return 1
    else:
        return 0


def find_next(n, m, input):
    width = len(input[0])
    height = len(input)
    if n < 0 or m < 0 or n > height - 1 or m > width - 1:
        return 'X'
    else:
        return input[n][m]


if __name__ == "__main__":
    main()
