import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input15.txt", "r")
    text = f.read()
    steps = text.split(',')
    the_sum = 0

    for step in steps:
        x = 0
        for char in step:
            x += ord(char)
            x *= 17
            x = x % 256
        the_sum += x

    print(the_sum)

    boxes = []
    for x in range(256):
        boxes.append({})

    for step in steps:
        if '=' in step:
            label, focus = step.split('=')
            hashed = hash(label)
            box = boxes[hashed]
            num = len(box) + 1
            if label in box.keys():
                num = list(box[label].keys())[0]
            box[label] = {num: int(focus)}
        else:
            label = step.replace('-', '')
            hashed = hash(label)
            box = boxes[hashed]
            if label in box.keys():
                num = list(box[label].keys())[0]
                box.pop(label)
                for label in box.keys():
                    num1 = list(box[label].keys())[0]
                    if num1 > num:
                        focus = box[label][num1]
                        box[label].pop(num1)
                        box[label][num1-1] = focus

    the_sum = 0
    for x in range(256):
        box = boxes[x]
        for label in box:
            num = list(box[label].keys())[0]
            focus = box[label][num]
            the_sum += (x + 1) * num * focus

    print(the_sum)


def hash(chars):
    x = 0
    for char in chars:
        x += ord(char)
        x *= 17
        x = x % 256
    return x


def compare_maps(map1, map2):
    same = True
    for k in range(len(map1)):
        if map1[k] != map2[k]:
            same = False
            break
    return same


def print_map(a_map):
    for x in range(len(a_map)):
        str_x = str(x)
        if x < 10:
            str_x = f'00{x}'
        elif x < 100:
            str_x = f'0{x}'
        print(f'{str_x}: {a_map[x]}')


def set_point(a_map, x, y, char):
    a_map[y] = a_map[y][:x] + char + a_map[y][x+1:]


if __name__ == "__main__":
    main()
