import argparse
import sys
import re
import os, os.path


def main():
    f = open("input3.txt", "r")
    text = f.read()
    input = text.split('\n')
    width = len(input[0])
    length = len(input)
    sum = 0

    for y in range(length):
        buffer = ''
        startx = -2
        for x in range(width):
            char = input[y][x]
            if char in '1234567890':
                buffer += char
                if startx == -2:
                    startx = x-1
            else:
                if buffer != '':
                    if y != 0: starty = y-1
                    else: starty = y
                    if y != length-1: endy = y+1
                    else: endy = y
                    part = False
                    for i in range(startx,x+1):
                        for k in range(starty,endy+1):
                            if input[k][i] not in '1234567890.':
                                part = True
                                break
                    if part:
                        sum += int(buffer)
                    buffer = ''
                    startx = -2

        if buffer != '':
            if y != 0:
                starty = y - 1
            else:
                starty = y
            if y != length - 1:
                endy = y + 1
            else:
                endy = y
            part = False
            for i in range(startx, width):
                for k in range(starty, endy + 1):
                    if input[k][i] not in '1234567890.':
                        part = True
                        break
            if part:
                sum += int(buffer)

    print(f'sum: {sum}')

    sum = 0
    gears = []
    parts = []
    for y in range(length):
        buffer = ''
        startx = -2
        for x in range(width):
            char = input[y][x]
            if char in '1234567890':
                buffer += char
                if startx == -2:
                    startx = x
            else:
                if char == '*':
                    gear = {
                        'x': x,
                        'y': y
                    }
                    gears.append(gear)
                if buffer != '':
                    part = {
                        'x1': startx,
                        'x2': x-1,
                        'y': y,
                        'num': int(buffer)
                    }
                    parts.append(part)
                    buffer = ''
                    startx = -2

        if buffer != '':
            part = {
                'x1': startx,
                'x2': width - 1,
                'y': y,
                'num': int(buffer)
            }
            parts.append(part)

    for gear in gears:
        counter = 0
        gear_ratio = 1
        for part in parts:
            if part['x1'] - 1 <= gear['x'] <= part['x2'] + 1:
                if part['y'] - 1 <= gear['y'] <= part['y'] + 1:
                    counter += 1
                    gear_ratio *= part['num']
                    if counter > 2:
                        break
        if counter == 2:
            sum += gear_ratio
    print(f'sum: {sum}')


if __name__ == "__main__":
    main()
