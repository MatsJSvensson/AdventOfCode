import argparse
import sys
import re
import os, os.path
import math

def main():
    f = open("input.txt", "r")
    input = f.read().split('\n')

    theSum = 0
    for line in input:
        theSum += int(evaluateLine2(evaluateLine1(line)))
    print(theSum)



def evaluateLine1(line):
    result = 0
    current = 'first'
    x = -1
    begin = 0
    adder = 0
    while(x < len(line)):
        x += 1
        char = line[x]
        if char in '1234567890':
            start = x
            if current is not '+':
                begin = x
            if x +1 < len(line):
                while (line[x + 1] in '1234567890'):
                    x += 1
                    if x+1 == len(line):
                        break
            num = int(line[start:x + 1])
            if current is '+':
                num += adder
                line = line.replace(line[begin:x+1],str(num))
                current = ''
                adder = num
                x = begin + len(str(num)) - 1
            elif current is 'first':
                adder = num
        if char is '(':
            line = evaluateParenthesis(line,x)
            x -= 1
        if char is '+':
            current = '+'
        if char is '*':
            current = 'first'
            adder = 0

        #print(result)
        if x + 1 >= len(line):
            break
    return line

def evaluateLine2(line):
    result = 1
    x = -1
    while(x+1 < len(line)):
        x += 1
        char = line[x]
        if char in '1234567890':
            start = x
            if x +1 < len(line):
                while(line[x+1] in '1234567890'):
                    x += 1
                    if x+1 == len(line):
                        break
            num = int(line[start:x+1])
            result *= num
    return str(result)


def evaluateParenthesis(line, index):
    x = index
    while(x+1 < len(line)):
        x += 1
        char = line[x]
        if char is ')':
            temp = evaluateLine1(line[index+1:x])
            temp = evaluateLine2(temp)
            line = line.replace(line[index:x+1],temp)
            return line
        if char is '(':
            line = evaluateParenthesis(line,x)
            hej = len(line)
            hej = hej
    exit(1)


if __name__ == "__main__":
    main()