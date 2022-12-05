import argparse
import sys
import re
import os, os.path


def main():
    f = open("input5.txt", "r")
    input = f.read().split('\n\n')
    stacks_raw = input[0].split('\n')
    moves = input[1].split('\n')
    height = len(stacks_raw)
    stacks = ['','','','','','','','','','']

    for n in range(2, height+1):
        for m in range(9):
            if stacks_raw[-n][m*4+1] != ' ':
                stacks[m] += stacks_raw[-n][m*4+1]

    stacks2 = stacks.copy()

    for move in moves:
        splits = move.split(' ')
        number = int(splits[1])
        col_from = int(splits[3]) - 1
        col_to = int(splits[5]) - 1

        for n in range(number):
            length = len(stacks[col_from])
            char = stacks[col_from][-1]
            stacks[col_from] = stacks[col_from][:length-1]
            stacks[col_to] += char

    result = ''

    for n in range(9):
        result += stacks[n][-1]

    for move in moves:
        splits = move.split(' ')
        number = int(splits[1])
        col_from = int(splits[3]) - 1
        col_to = int(splits[5]) - 1

        length = len(stacks2[col_from])
        chars = stacks2[col_from][length-number:]
        stacks2[col_from] = stacks2[col_from][:length-number]
        stacks2[col_to] += chars

    result2 = ''

    for n in range(9):
        result2 += stacks2[n][-1]

    print(f'counter: {result}')
    print(f'counter: {result2}')


if __name__ == "__main__":
    main()
