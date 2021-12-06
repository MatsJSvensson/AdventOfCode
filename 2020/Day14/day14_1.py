import argparse
import sys
import re
import os, os.path
import math

def main():
    f = open("input.txt", "r")
    input = f.read().split('\n')

    memory = dict()
    mask = ''

    for line in input:
        if 'mem' in line:
            vals = line.split(' = ')
            value = int(vals[1])
            adress = int(vals[0].replace('mem[','').replace(']',''))
            value = applyMask(value,mask)
            memory[adress] = value

        elif 'mask' in line:
            line = line.replace('mask = ', '')
            mask = line

    sum = 0
    for key in memory.keys():
        sum += memory[key]

    print("Sum: {}".format(sum))

def applyMask(val, mask):
    newVal = 0
    base2 = ''
    new2 = ''
    for x in range(36):
        divider = pow(2, 35 - x)
        bit = math.floor(val / divider)
        val = val % divider
        print(bit)
        base2 += str(bit)
        if mask[x] is not 'X':
            bit = int(mask[x])
        newVal += bit*divider
        new2 += str(bit)

    print(base2)
    print(mask)
    print(new2)
    print('\n')

    return int(newVal)


if __name__ == "__main__":
    main()