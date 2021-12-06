import argparse
import sys
import re
import os, os.path
import math


def main():
    input = '167248359'
    cups = []
    theDict = {}
    nCups = 1000000

    for char in input:
        cups.append(int(char))
    for x in range(10,nCups+1):
        cups.append(x)
    for x in range(1,nCups):
        theDict[cups[x-1]] = cups[x]
    theDict[nCups] = 1

    currentVal = 1
    for x in range(10000000):
        one = theDict[currentVal]
        two = theDict[one]
        three = theDict[two]
        dest = currentVal - 1
        while dest in [one,two,three,0]:
            dest -= 1
            if dest <= 0:
                dest = nCups
        theDict[currentVal] = theDict[three]
        theDict[three] = theDict[dest]
        theDict[dest] = one

        currentVal = theDict[currentVal]

        if x % 100000 == 0:
            print(x / 100000)

    first = theDict[1]
    second = theDict[first]
    print(first * second)






if __name__ == "__main__":
    main()