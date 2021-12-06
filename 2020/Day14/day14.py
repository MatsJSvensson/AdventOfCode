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
            adresses = applyMask(mask,adress)
            for dress in adresses:
                memory[dress] = value

        elif 'mask' in line:
            line = line.replace('mask = ', '')
            mask = line

    sum = 0
    for key in memory.keys():
        sum += memory[key]

    print("Sum: {}".format(sum))

def applyMask(mask, adress):
    base2 = ''
    adresses = [0]
    for x in range(36):
        divider = pow(2, 35 - x)
        bit = math.floor(adress / divider)
        adress = adress % divider
        base2 += str(bit)
        if mask[x] is '0':
            length = len(adresses)
            for x in range(length):
                adresses[x] += bit*divider
        elif mask[x] is '1':
            length = len(adresses)
            for x in range(length):
                adresses[x] += divider
        elif mask[x] is 'X':
            length = len(adresses)
            for x in range(length):
                adresses.append(adresses[x])
                adresses[x] += divider

        else:
            print("Odd input: ".format(mask[x]))

    print(base2)
    print(mask)
    print(adresses)
    print('\n')

    return adresses


if __name__ == "__main__":
    main()