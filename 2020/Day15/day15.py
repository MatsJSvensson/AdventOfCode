import argparse
import sys
import re
import os, os.path
import math

def main():
    input = [7,12,1,0,16,2]
    lastIndex = dict()

    start = len(input)
    for x in range(start):
        lastIndex[input[x]] = x

    answer = 0
    for x in range(start,30000000):
        lastAnswer = input[x-1]
        if lastAnswer in lastIndex.keys():
            answer = x-1 - lastIndex[lastAnswer]
        else:
            answer = 0
        lastIndex[lastAnswer] = x - 1
        #print(answer)
        input.append(answer)
        if(x%100000 == 0):
            print(x)

    #print(input)
    print(answer)
    print(len(input))



if __name__ == "__main__":
    main()