import argparse
import sys
import re
import os, os.path


def main():
    f = open("input4.txt", "r")
    text = f.read()
    input = text.split('\n')
    width = len(input[0])
    length = len(input)
    the_sum = 0

    for line in input:
        x = 0
        winning, numbers = line.split(':')[1].split(' | ')
        winning = winning.split(' ')
        numbers = numbers.split(' ')
        for win in winning:
            if win == '':
                pass
            elif win in numbers:
                if x == 0:
                    x = 1
                else:
                    x *= 2
        the_sum += x

    print(f'sum: {the_sum}')
    the_sum = 0
    copies = {}
    for line in input:
        x = 0
        winning, numbers = line.split(':')[1].split(' | ')
        winning = winning.split(' ')
        numbers = numbers.split(' ')
        for win in winning:
            if win == '':
                pass
            elif win in numbers:
                x += 1

        addition = sum(copies.values()) + 1
        the_sum += addition

        if x in copies.keys():
            copies[x] += addition
        else:
            copies[x] = addition
        max_val = max(copies.keys())
        for n in range(max_val+1):
            if n in copies.keys():
                if n == 0:
                    copies[n] = 0
                else:
                    copies[n-1] = copies[n]
                    copies[n] = 0
        pass

        # for n in range(len(copies)):
        #     copies[n] -= 1
        # addition = 1 + len(copies)
        # sum += addition
        # for n in range(len(copies)+1):
        #     copies.append(x)
        # t = copies.count(0)
        # for n in range(t):
        #     copies.remove(0)

    print(f'sum: {the_sum}')


if __name__ == "__main__":
    main()
