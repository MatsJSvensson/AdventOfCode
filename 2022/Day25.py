import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input25.txt", "r")
    text = f.read()
    snafus = text.split('\n')
    a_sum = 0
    for snafu in snafus:
        dec = int(snafu2dec(snafu))
        print(f'{dec} {dec2snafu(dec)}')
        a_sum += dec

    print(f'{a_sum} {dec2snafu(a_sum)}')


def snafu2dec(snafu):
    length = len(snafu)
    a_sum = 0
    for n in range(length):
        value = snafu[n]
        if value == '-':
            value = -1
        elif value == '=':
            value = -2
        else:
            value = int(value)
        a_sum += value * math.pow(5, length-n-1)
    return int(a_sum)


def dec2snafu(dec):
    n = 0
    while (math.pow(5, n) - 1)/2 < dec:
        n += 1
    n -= 1
    snafu = ''
    for x in range(n):
        value = 0
        while abs(dec) > (math.pow(5, n-x) - 1) / 2:
            if dec > 0:
                value += 1
                dec -= math.pow(5, n-x)
            elif dec < 0:
                value -= 1
                dec += math.pow(5, n-x)
        if value == -2:
            snafu += '='
        elif value == -1:
            snafu += '-'
        else:
            snafu += str(int(value))
    if dec == -2:
        snafu += '='
    elif dec == -1:
        snafu += '1'
    else:
        snafu += str(int(dec))
    return snafu


if __name__ == "__main__":
    main()
