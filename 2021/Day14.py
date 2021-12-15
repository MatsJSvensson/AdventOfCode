import argparse
import sys
import re
import os, os.path
import math

def main():
    f = open("input14.txt", "r")
    template, instructions = f.read().split('\n\n')
    instructions = instructions.split('\n')
    print(template)
    results = {}

    for t in range(40):
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

if __name__ == "__main__":
    main()