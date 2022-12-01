import argparse
import sys
import re
import os, os.path
import math

def main():
    f = open("input14.txt", "r")
    orig_template, instructions = f.read().split('\n\n')
    template = orig_template
    instructions = instructions.split('\n')
    print(template)
    results = {}

    for t in range(10):
        new_template = ''
        for n in range(len(template)-1):
            pair = template[n:n + 2]
            for instruction in instructions:
                if len(instruction) > 1:
                    start, out = instruction.split(' -> ')
                    if pair == start:
                        new_template += template[n] + out
                        break
        new_template += template[-1]
        template = new_template
        print(len(template))

    for char in template:
        if char not in results.keys():
            results[char] = 0

        results[char] += 1

    result = max(results.values()) - min(results.values())

    print(results)
    print(result)

    memo_map = {}
    for key in results.keys():
        results[key] = 0

    for instruction in instructions:
        if len(instruction) > 1:
            start, out = instruction.split(' -> ')
            pair1 = start[0] + out
            pair2 = out + start[1]
            memo_map[start] = [pair1, pair2, out]

    for n in range(len(orig_template)-1):
        pair = template[n:n + 2]
        recurse(pair, memo_map, results, 30)
        print(pair)

    result = max(results.values()) - min(results.values())

    print(results)
    print(result)


def recurse(pair, memo_map, results, counter):
    counter -= 1
    results[memo_map[pair][2]] += 1
    if counter > 0:
        recurse(memo_map[pair][0], memo_map, results, counter)
        recurse(memo_map[pair][1], memo_map, results, counter)



if __name__ == "__main__":
    main()