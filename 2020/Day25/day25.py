import argparse
import sys
import re
import os, os.path
import math

eight = []
eleven = []
fortytwo = []
thirtyone = []

def main():
    f = open("input.txt", "r")
    input = f.read().split('\n')

    sizes = list(map(findLoopSize,map(int,input)))

    print(sizes)

    print(findEncryption(sizes[1], int(input[0])))
    print(findEncryption(sizes[0], int(input[1])))

def findLoopSize(publicKey):

    x = 0
    value = 1
    while(value != publicKey):
        value *= 7
        value = value % 20201227
        x += 1
    return x

def findEncryption(loopSize,publicKey):
    value = 1
    for x in range(loopSize):
        value *= publicKey
        value = value % 20201227
    return value


if __name__ == "__main__":
    main()