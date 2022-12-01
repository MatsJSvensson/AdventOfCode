import argparse
import sys
import re
import os, os.path


def main():
    f = open("input1.txt", "r")
    input = f.read().split('\n\n')
    cal_list = []
    for elf in input:
        lines = elf.split('\n')
        calories = 0
        for line in lines:
            calories += int(line)
        print(calories)
        cal_list.append(calories)
    max1 = max(cal_list)
    cal_list.remove(max1)
    max2 = max(cal_list)
    cal_list.remove(max2)
    max3 = max(cal_list)
    top3 = max1 + max2 + max3

    print(f'max: {max1}')
    print(f'top3: {top3}')


if __name__ == "__main__":
    main()
