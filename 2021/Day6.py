import argparse
import sys
import re
import os, os.path
import math

def main():
    f = open("input6.txt", "r")
    fishes = f.readline().split(',')
    fishBoxes = [0,0,0,0,0,0,0,0,0]

    for fish in fishes:
        fishBoxes[int(fish)] += 1
    print(fishBoxes)

    for n in range(256):
        new_fish = fishBoxes[0]
        for m in range(8):
            fishBoxes[m] = fishBoxes[m+1]
        fishBoxes[8] = new_fish
        fishBoxes[6] += new_fish

        print(fishBoxes)

    print(f'fishBoxes: {fishBoxes}, sum: {sum(fishBoxes)}')





if __name__ == "__main__":
    main()