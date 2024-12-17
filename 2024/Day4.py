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
    word = 'XMAS'

    for n in range(height):
        for m in range(width):
            if input[n][m] == 'X':
                nFound = find_first(n, m, word, input)
                the_sum += nFound

    print(f'The sum = {the_sum}')


def find_first(n, m, word, input):
    a_sum = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if not (x == 0 and y == 0):
                a_sum += find_next(n + x, m + y, word, 1, input, [x, y])
    return a_sum


def find_next(n, m, word, x, input, dir):
    width = len(input[0])
    height = len(input)
    if n < 0 or m < 0 or n > height - 1 or m > height - 1:
        return 0

    if word[x] == input[n][m]:
        x += 1
        a_sum = 0
        if x == len(word):
            return 1

        a_sum += find_next(n + dir[0], m + dir[1], word, x, input, dir)

        return a_sum
    else:
        return 0


if __name__ == "__main__":
    main()
