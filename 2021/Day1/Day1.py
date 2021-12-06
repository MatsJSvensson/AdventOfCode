import argparse
import sys
import re
import os, os.path

def main():
    f = open("day1.txt", "r")
    input = f.read().split('\n')
    current = int(input[0])
    ints = [current]
    amount = 0
    for line in input[1:]:
        new_depth = int(line)
        if new_depth > current:
            amount += 1
        current = new_depth
        ints.append(current)

    print(amount)

    amount = 0
    current = sum(ints[0:3])
    print(current)
    for i in range(0,len(ints)-2):
        new_sum = sum(ints[i:i+3])
        if new_sum > current:
            amount += 1
        current = new_sum

    print(amount)



if __name__ == "__main__":
    main()