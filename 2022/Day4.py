import argparse
import sys
import re
import os, os.path


def main():
    f = open("input4.txt", "r")
    input = f.read().split('\n')
    counter = 0
    counter2 = 0
    for line in input:
        elf1, elf2 = line.split(',')
        elf1_list = elf1.split('-')
        elf2_list = elf2.split('-')
        start1 = int(elf1_list[0])
        start2 = int(elf2_list[0])
        end1 = int(elf1_list[1])
        end2 = int(elf2_list[1])
        if start1 >= start2 and end1 <= end2:
            counter += 1
            counter2 += 1
        elif start1 <= start2 and end1 >= end2:
            counter += 1
            counter2 += 1
        elif start1 <= start2 <= end1:
            counter2 += 1
        elif start1 <= end2 <= end1:
            counter2 += 1

    print(f'counter: {counter}')
    print(f'counter2: {counter2}')


if __name__ == "__main__":
    main()
