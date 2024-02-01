import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input9.txt", "r")
    text = f.read()
    lines = text.split('\n')
    the_sum = 0

    for line in lines:
        sequence = line.split(' ')
        new_val = solver(sequence)
        the_sum += new_val
        print(new_val)
    print(the_sum)

    the_sum = 0

    for line in lines:
        sequence = line.split(' ')
        new_val = solver(sequence)
        the_sum += new_val
        print(new_val)
    print(the_sum)


def solver(sequence):
    new_seq = []
    new_len = len(sequence)-1
    for x in range(new_len):
        diff = int(sequence[x+1]) - int(sequence[x])
        new_seq.append(diff)

    if new_seq.count(0) == new_len:
        return int(sequence[-1])
    else:
        new_diff = solver(new_seq)
        return int(sequence[0]) - new_diff


def solver2(sequence):
    new_seq = []
    new_len = len(sequence)-1
    for x in range(new_len):
        diff = int(sequence[x+1]) - int(sequence[x])
        new_seq.append(diff)

    if new_seq.count(0) == new_len:
        return int(sequence[-1])
    else:
        new_diff = solver(new_seq)
        return int(sequence[-1]) + new_diff


if __name__ == "__main__":
    main()
