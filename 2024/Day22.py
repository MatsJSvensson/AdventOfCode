import argparse
import sys
import re
import os, os.path
import math
import aoc_utils as utils

f = open("input22.txt", "r")
text = f.read()
parts = text.split('\n')
seeds = [int(x) for x in parts]


def main():
    the_sum = 0
    a_dict = {}
    sequence_dict = {}
    for seed in seeds:
        s = seed
        s1 = 0
        s2 = 0
        s3 = 0
        s4 = 0
        price = seed % 10
        sequence_list = []
        for i in range(2000):
            s = generate(s, a_dict)
            old_price = price
            price = s % 10
            s4 = s3
            s3 = s2
            s2 = s1
            s1 = price - old_price
            if i >= 3:
                name = f'{s4}_{s3}_{s2}_{s1}'
                if name not in sequence_list:
                    sequence_list.append(name)
                    if name in sequence_dict.keys():
                        sequence_dict[name] += price
                    else:
                        sequence_dict[name] = price

        the_sum += s
    print(the_sum)
    new_list = sequence_dict.values()
    maximum = max(new_list)
    print(sequence_dict['-2_1_-1_3'])
    print(maximum)


def generate(seed, a_dict):
    if seed in a_dict.keys():
        return a_dict[seed]
    a = 64 * seed
    new_seed = a ^ seed
    new_seed = prune(new_seed)
    b = int(new_seed/32)
    new_seed = b ^ new_seed
    new_seed = prune(new_seed)
    c = new_seed * 2048
    new_seed = c ^ new_seed
    new_seed = prune(new_seed)
    a_dict[seed] = new_seed
    return new_seed


def prune(num):
    return num % 16777216


if __name__ == "__main__":
    main()
