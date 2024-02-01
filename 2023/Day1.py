import argparse
import sys
import re
import os, os.path


def main():
    f = open("input1.txt", "r")
    text = f.read()
    # text = text.replace('one', '1')
    # text = text.replace('two', '2')
    # text = text.replace('three', '3')
    # text = text.replace('four', '4')
    # text = text.replace('five', '5')
    # text = text.replace('six', '6')
    # text = text.replace('seven', '7')
    # text = text.replace('eight', '8')
    # text = text.replace('nine', '9')
    # text = text.replace('zero', '0')
    input = text.split('\n')
    sum = 0
    digits = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    for line in input:
        first = ''
        last = ''
        buffer = ''
        for char in line:
            buffer += char
            for digit in digits.keys():
                if digit in buffer:
                    buffer = char
                    char = digits[digit]
                    break
            if char in '1234567890':
                if first == '':
                    first = char
                last = char
                if char in buffer:
                    buffer = ''

        number = first + last
        print(f'{line}: {number}')
        sum += int(number)

    print(f'sum: {sum}')


if __name__ == "__main__":
    main()
