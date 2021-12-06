import argparse
import sys
import re
import os, os.path

def main():
    f = open("input.txt", "r")
    input = f.read().split('\n')

    max = 0
    for x in range(len(input)):
        input[x] = int(input[x])
        if input[x] > max:
            max = input[x]
    diff = 1
    ones = 0
    twoes = 0
    threes = 0
    for x in range(1,max+1):
        if x in input:
            if diff == 1:
                ones += 1
            if diff == 2:
                twoes += 1
            if diff == 3:
                threes += 1
            diff = 1
        else:
            diff += 1

    print("{} * {} = {}".format(ones,threes,ones * (threes+1)))

    input.append(0)
    input.sort()

    lists = []
    oldX = 0
    for x in range(len(input)-1):
        if input[x+1] - input[x] == 3:
            lists.append(input[oldX:x+1])
            oldX = x+1
    lists.append(input[oldX:])
    print(lists)
    sum = 1
    for list in lists:
        if len(list) > 2:
            sum *= recursive2(list)
    print(sum)
    pathMapping(max,input)


def pathMapping(max, input):
    pathMap = [0]*(max+1)
    pathMap[0] = 1
    for x in input:
        for y in range(1,4):
            if x+y in input:
                pathMap[x+y] += pathMap[x]
    print(pathMap[max])



def recursive2(input):
    sum = 0
    L = len(input)
    base = input[0]
    #print(input)
    if L > 1:
        input.pop(0)
        sum += recursive2(input.copy())
    else:
        return 1
    if L > 2:
        if input[1] - base <= 3:
            input.pop(0)
            sum += recursive2(input.copy())
    if L > 3:
        if input[1] - base <= 3:
            input.pop(0)
            sum += recursive2(input.copy())
    return sum

def recursive(input, val, max):
    newVal = 0
    y = 0
    for x in input:
        if x - y > 3:
            return 0
        if x > val:
            newVal = x
            break
        y = x
    input2 = input.copy()
    input2.remove(val)
    #print("{} {}".format(val,newVal))
    if val == max or newVal == 0:
        #print(input)
        sum = 0
        sum += checkSet(input, max)
        #print(input2)
        sum += checkSet(input2,max)
        return sum
    else:
        return recursive(input,newVal,max) + recursive(input2,newVal,max)


def checkSet(input, max):
    diff = 1
    for x in range(1,max+1):
        if x in input:
            diff = 1
        else:
            diff += 1
        if diff > 3:
            return 0
    return 1



if __name__ == "__main__":
    main()