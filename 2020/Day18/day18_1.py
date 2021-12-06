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
        theSum += evaluateLine(line)
    print(theSum)



def evaluateLine(line):
    line += ' '
    result = 0
    current = 'first'
    x = -1
    while(x < len(line)):
        x += 1
        char = line[x]
        if char is '(':
            line = evaluateParenthesis(line,x)
            x -= 1
        if char is '+':
            current = '+'
        if char is '*':
            current = '*'
        if char in '1234567890':
            start = x
            while(line[x+1] in '1234567890'):
                x += 1
            num = int(line[start:x+1])
            if current == 'first':
                result = num
            if current is '+':
                result += num
            if current is '*':
                result *= num
        #print(result)
        if x + 1 >= len(line):
            break
    return result

def evaluateParenthesis(line, index):
    for x in range(index+1,len(line)):
        if line[x] is ')':
            num = evaluateLine(line[index+1:x] + ' ')
            line = line.replace(line[index:x+1],str(num))
            return line
        if line[x] is '(':
            line = evaluateParenthesis(line,x)
    exit(1)








if __name__ == "__main__":
    main()