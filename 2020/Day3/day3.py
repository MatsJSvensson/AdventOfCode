import argparse
import sys
import re
import os, os.path

def main():
    f = open("input.txt", "r")
    input = f.read().split('\n')
    product = 1
    product = product * skiSlope(input, 1, 1)
    product = product * skiSlope(input, 1, 3)
    product = product * skiSlope(input, 1, 5)
    product = product * skiSlope(input, 1, 7)
    product = product * skiSlope(input, 2, 1)
    print("Product: {}".format(product))


def skiSlope(input, angleDown, angleRight):
    angle = angleRight
    down = angleDown
    width = 31

    count = 0
    position = 0
    trees = 0
    for line in input:
        if count % down == 0:
            position = position % width
            if line[position] is '.':
                print(line[0:position] + 'O' + line[position + 1:width])
            elif line[position] is '#':
                print(line[0:position] + 'X' + line[position + 1:width])
                trees = trees + 1
            else:
                #print("weird character")
                quit(1)
            position = position + angle
        else:
            print(line)
        count = count + 1
    print("Trees: {}".format(trees))

    return trees


if __name__ == "__main__":
    main()