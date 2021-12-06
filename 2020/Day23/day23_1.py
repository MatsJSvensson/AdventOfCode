import argparse
import sys
import re
import os, os.path
import math


def main():
    input = '167248359'
    currentPos = 0


    for x in range(100):
        currentVal = int(input[currentPos])
        print(input.replace(str(currentVal), "({})".format(str(currentVal))))
        double = input + input
        three = double[currentPos + 1:currentPos + 4]
        for char in three:
            double = double.replace(char, '')

        lowerVal = currentVal - 1
        if lowerVal == 0:
            lowerVal = 9
        while(str(lowerVal) not in double):
            lowerVal -= 1
            if lowerVal == 0:
                lowerVal = 9

        double = double.replace(str(lowerVal),str(lowerVal) + three)
        input = double[:9]

        currentPos = input.index(str(currentVal)) + 1
        currentPos = currentPos % 9

    print(input.replace(str(currentVal), "({})".format(str(currentVal))))
    index = input.index('1')
    print(double[index:index+9])






if __name__ == "__main__":
    main()