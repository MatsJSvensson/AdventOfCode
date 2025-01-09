import argparse
import sys
import re
import os, os.path
import math
import aoc_utils as utils

f = open("input21.txt", "r")
text = f.read()
codes = text.split('\n')

numpad = {'7': [0, 0],
          '8': [1, 0],
          '9': [2, 0],
          '4': [0, 1],
          '5': [1, 1],
          '6': [2, 1],
          '1': [0, 2],
          '2': [1, 2],
          '3': [2, 2],
          '': [0, 3],
          '0': [1, 3],
          'A': [2, 3]}

keypad = {'': [0, 0],
          '^': [1, 0],
          'A': [2, 0],
          '<': [0, 1],
          'v': [1, 1],
          '>': [2, 1]}


def main():
    the_sum = 0
    for code in codes:
        print(code)
        step1 = pad_translator([2, 3], code, numpad)
        print(step1)
        step2 = []
        for s in step1:
            step2.extend(pad_translator([2, 0], s, keypad))
        print(step2)
        step3 = []
        for s in step2:
            step3.extend(pad_translator([2, 0], s, keypad))
        # print(step3)

        num = int(code.replace('A', ''))
        lengths = [len(x) for x in step3]
        length = min(lengths)
        the_sum += length * num
    print(the_sum)

    memo_map = {}
    the_sum = 0
    for code in codes:
        print(code)
        step1 = pad_translator([2, 3], code, numpad)
        print(step1)
        step2 = []
        for s in step1:
            commands = split_command(s)
            new_command = ''
            for command in commands:
                new_command += keypad_translator([2, 0], command, True, memo_map)
            step2.append(new_command)
        print(step2)
        step3 = []
        for s in step2:
            commands = split_command(s)
            new_command = ''
            for command in commands:
                new_command += keypad_translator([2, 0], command, True, memo_map)
            step3.append(new_command)
        print(step3)

        num = int(code.replace('A', ''))
        lengths = [len(x) for x in step3]
        length = min(lengths)
        the_sum += length * num
    print(the_sum)


def split_command(s):
    s_list = s.split('A')
    res = [x + 'A' for x in s_list]
    l = len(res)
    return res[:l-1]


def pad_translator(start, code, pad):
    if pad[''][0] == start[0] and pad[''][1] == start[1]:
        return []
    char = code[0]
    pos = pad[char]
    x = pos[0] - start[0]
    y = pos[1] - start[1]
    new_codes = []
    if x > 0:
        res = pad_translator([start[0] + x, start[1]], code, pad)
        for c in res:
            new_codes.append('>' * x + c)
    elif x < 0:
        res = pad_translator([start[0] + x, start[1]], code, pad)
        for c in res:
            new_codes.append('<' * abs(x) + c)
    if y < 0:
        res = pad_translator([start[0], start[1] + y], code, pad)
        for c in res:
            new_codes.append('^' * abs(y) + c)
    elif y > 0:
        res = pad_translator([start[0], start[1] + y], code, pad)
        for c in res:
            new_codes.append('v' * y + c)

    if x == 0 and y == 0:
        if len(code) > 1:
            res = pad_translator(start, code[1:], pad)
            for c in res:
                new_codes.append('A' + c)
        else:
            new_codes = ['A']

    return new_codes


def keypad_translator(start, code, save, memo_map):
    if code in memo_map.keys():
        return memo_map[code]
    char = code[0]
    pos = keypad[char]
    x = pos[0] - start[0]
    y = pos[1] - start[1]
    new_code = ''
    if x < 0:
        new_code += '<' * abs(x)
    if y > 0:
        new_code += 'v' * y
    if x > 0:
        new_code += '>' * x
    if y < 0:
        new_code += '^' * abs(y)

    new_code += 'A'

    if len(code) > 1:
        new_code += keypad_translator(pos, code[1:], False, memo_map)
    if save:
        memo_map[code] = new_code
    return new_code


if __name__ == "__main__":
    main()
