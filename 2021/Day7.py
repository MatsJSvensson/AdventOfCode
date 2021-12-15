import argparse
import sys
import re
import os, os.path
import math

def main():
    f = open("input7.txt", "r")
    crabs = f.readline().split(',')
    nCrabs = len(crabs)
    max = 0

    for n in range(nCrabs):
        crabs[n] = int(crabs[n])
        if crabs[n] > max:
            max = crabs[n]

    min_fuel = 1000000
    align = 0
    for n in range(max):
        the_sum = 0
        for crab in crabs:
            the_sum += math.fabs(crab - n)
        if the_sum < min_fuel:
            min_fuel = the_sum
            align = n

    print(f'min fuel: {min_fuel}, align: {align}')

    min_fuel = 1000000000
    align = 0
    for n in range(max):
        the_sum = 0
        for crab in crabs:
            the_sum += sum(range(int(math.fabs(crab - n)+1)))
        if the_sum < min_fuel:
            min_fuel = the_sum
            align = n

    print(f'min fuel: {min_fuel}, align: {align}')



if __name__ == "__main__":
    main()