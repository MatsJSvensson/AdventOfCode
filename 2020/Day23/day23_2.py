import argparse
import sys
import re
import os, os.path
import math


def main():
    input = '167248359'
    currentPos = 0
    cups = []
    nCups = 1000000

    for char in input:
        cups.append(int(char))
    for x in range(10,nCups+1):
        cups.append(x)

    for x in range(10000000):
        currentVal = cups[currentPos]
        #print("{} {}".format(currentVal,cups[:20]))
        #print(input.replace(str(currentVal), "({})".format(str(currentVal))))
        #double = input + input
        three = []
        tempList = []
        for i in range(3):
            temp = (currentPos+i+1) % nCups
            three.append(cups[temp])
            tempList.append(temp)
        for i in range(3):
            temp = max(tempList)
            cups.pop(temp)
            tempList.remove(temp)

        lowerVal = currentVal - 1
        if lowerVal == 0:
            lowerVal = nCups
        while(lowerVal in three):
            lowerVal -= 1
            if lowerVal == 0:
                lowerVal = nCups

        index = cups.index(lowerVal)
        for i in range(3):
            temp = (index + i + 1) % nCups
            cups.insert(temp,three[i])

        currentPos = cups.index(currentVal) + 1
        currentPos = currentPos % nCups


        fraction = x / 100000
        print(fraction)

    index = cups.index(1)
    first = cups[index+1]
    second = cups[index + 2]
    print(first * second)






if __name__ == "__main__":
    main()