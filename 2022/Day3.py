import argparse
import sys
import re
import os, os.path


def main():
    f = open("input3.txt", "r")
    input = f.read().split('\n')
    prio_list = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total_score = 0
    for line in input:
        length = len(line)
        half = int(length/2)
        item = '0'
        for char in line[:half]:
            if char in line[half:]:
                item = char
                break
        prio = prio_list.find(item)
        total_score += prio

    total_prio = 0
    total_length = len(input)
    groups = int(total_length/3)
    item = '0'
    for n in range(groups):
        for char in input[n*3]:
            if char in input[n*3+1] and char in input[n*3+2]:
                item = char
                break
        prio = prio_list.find(item)
        total_prio += prio

    print(f'total score: {total_score}')
    print(f'total prio: {total_prio}')


if __name__ == "__main__":
    main()
