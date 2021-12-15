import argparse
import sys
import re
import os, os.path
import math

def main():
    f = open("input10.txt", "r")
    the_input = f.readlines()

    startSymbols = '([{<'
    currentStarts = []
    pairings = { '(': ')', '[': ']', '{': '}', '<': '>'}
    corrupts = []
    incompletes = []

    for row in the_input:
        if len(row) > 1:
            corrupt = False
            currentStarts.clear()
            for char in row.strip():
                if char in startSymbols:
                    currentStarts.append(char)
                elif pairings[currentStarts[-1]] == char:
                    currentStarts.pop(-1)
                else:
                    corrupts.append(char)
                    corrupt = True
                    break
            if not corrupt:
                incompletes.append(row)

    the_sum = 0
    scores = { ')': 3, ']': 57, '}': 1197, '>': 25137}
    for char in corrupts:
        the_sum += scores[char]

    second_sum = 0
    temp_sums = []
    scores = { ')': 1, ']': 2, '}': 3, '>': 4}

    for row in incompletes:
        if len(row) > 1:
            currentStarts.clear()
            for char in row.strip():
                if char in startSymbols:
                    currentStarts.append(char)
                elif pairings[currentStarts[-1]] == char:
                    currentStarts.pop(-1)
            temp_sum = 0
            backwards = currentStarts.copy()
            backwards.reverse()
            for char in backwards:
                temp_sum *= 5
                temp_sum += scores[pairings[char]]
            temp_sums.append(temp_sum)

    temp_sums.sort()
    print(f'sums = {the_sum}, {temp_sums[math.floor(len(temp_sums)/2)]}')


if __name__ == "__main__":
    main()