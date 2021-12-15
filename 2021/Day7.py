import argparse
import sys
import re
import os, os.path
import math

def main():
    f = open("input7.txt", "r")
    crabs = f.readline().split(',')
    the_sum = 0
    nCrabs = len(crabs)
    max = 0

    for n in range(nCrabs):
        crabs[n] = int(crabs[n])
        the_sum += crabs[n]
        if crabs[n] > 0:
            max = crabs[n]

    middle = the_sum / float(nCrabs)
    lower = math.floor(middle)
    higher = math.ceil(middle)
    low = 0
    high = 0
    for crab in crabs:
        low += math.fabs(crab - lower)
        high += math.fabs(crab - higher)

    print(f'middle: {middle}, low: {low}, high: {high}')





if __name__ == "__main__":
    main()