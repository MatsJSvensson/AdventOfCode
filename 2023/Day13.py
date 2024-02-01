import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input13.txt", "r")
    text = f.read()
    parts = text.split('\n\n')
    the_sum = 0

    for part in parts:
        part = part.split('\n')
        done = False
        for x in range(len(part)-1):
            if part[x] == part[x+1]:
                valid = True
                if x + 1 <= len(part)/2:
                    for y in range(x):
                        if part[y] != part[2*x-y+1]:
                            valid = False
                            break
                if x + 1 > len(part)/2:
                    for y in range(len(part)-x-2):
                        if part[x+y+2] != part[x-y-1]:
                            valid = False
                            break
                if valid:
                    print(x)
                    the_sum += (x+1)*100
                    done = True
                    break

        if not done:
            for y in range(len(part[0])-1):
                valid = False
                if y + 1 <= len(part[0])/2:
                    if part[0][:y+1] == part[0][y+1:(y+1)*2][::-1]:
                        valid = True
                        for x in range(1, len(part)):
                            if part[x][:y+1] != part[x][y+1:(y+1)*2][::-1]:
                                p1 = part[x][:y+1]
                                p2 = part[x][y+1:(y+1)*2][::-1]
                                valid = False
                                break
                if y + 1 > len(part[0])/2:
                    if part[0][2*(y+1)-(len(part[0])):y+1] == part[0][y+1:][::-1]:
                        valid = True
                        for x in range(1, len(part)):
                            if part[x][2 * (y + 1) - (len(part[0])):y + 1] != part[x][y + 1:][::-1]:
                                valid = False
                                break
                if valid:
                    print(y)
                    the_sum += y+1
                    break
    print(the_sum)


    the_sum = 0

    for org_part in parts:
        org_part = org_part.split('\n')

        part = org_part.copy()
        done = False

        ignore_x = -1
        ignore_y = -1
        for x in range(len(part) - 1):
            if part[x] == part[x + 1]:
                valid = True
                if x + 1 <= len(part) / 2:
                    for y in range(x):
                        if part[y] != part[2 * x - y + 1]:
                            valid = False
                            break
                if x + 1 > len(part) / 2:
                    for y in range(len(part) - x - 2):
                        if part[x + y + 2] != part[x - y - 1]:
                            valid = False
                            break
                if valid:
                    ignore_x = x
                    done = True
                    break

        if not done:
            for y in range(len(part[0]) - 1):
                valid = False
                if y + 1 <= len(part[0]) / 2:
                    if part[0][:y + 1] == part[0][y + 1:(y + 1) * 2][::-1]:
                        valid = True
                        for x in range(1, len(part)):
                            if part[x][:y + 1] != part[x][y + 1:(y + 1) * 2][::-1]:
                                p1 = part[x][:y + 1]
                                p2 = part[x][y + 1:(y + 1) * 2][::-1]
                                valid = False
                                break
                if y + 1 > len(part[0]) / 2:
                    if part[0][2 * (y + 1) - (len(part[0])):y + 1] == part[0][y + 1:][::-1]:
                        valid = True
                        for x in range(1, len(part)):
                            if part[x][2 * (y + 1) - (len(part[0])):y + 1] != part[x][y + 1:][::-1]:
                                valid = False
                                break
                if valid:
                    ignore_y = y
                    break



        done = False
        for i in range(len(org_part)):
            for k in range(len(org_part[0])):
                part = org_part.copy()
                if part[i][k] == '#':
                    new_char = '.'
                else:
                    new_char = '#'
                part[i] = part[i][:k] + new_char + part[i][k+1:]
                a=1

                for x in range(len(part)-1):
                    if x == ignore_x:
                        continue
                    if part[x] == part[x+1]:
                        valid = True
                        if x + 1 <= len(part)/2:
                            for y in range(x):
                                if part[y] != part[2*x-y+1]:
                                    valid = False
                                    break
                        if x + 1 > len(part)/2:
                            for y in range(len(part)-x-2):
                                if part[x+y+2] != part[x-y-1]:
                                    valid = False
                                    break
                        if valid:
                            print(x)
                            the_sum += (x+1)*100
                            done = True
                            break

                if not done:
                    for y in range(len(part[0])-1):
                        if y == ignore_y:
                            continue
                        valid = False
                        if y + 1 <= len(part[0])/2:
                            if part[0][:y+1] == part[0][y+1:(y+1)*2][::-1]:
                                valid = True
                                for x in range(1, len(part)):
                                    if part[x][:y+1] != part[x][y+1:(y+1)*2][::-1]:
                                        p1 = part[x][:y+1]
                                        p2 = part[x][y+1:(y+1)*2][::-1]
                                        valid = False
                                        break
                        if y + 1 > len(part[0])/2:
                            if part[0][2*(y+1)-(len(part[0])):y+1] == part[0][y+1:][::-1]:
                                valid = True
                                for x in range(1, len(part)):
                                    if part[x][2 * (y + 1) - (len(part[0])):y + 1] != part[x][y + 1:][::-1]:
                                        valid = False
                                        break
                        if valid:
                            print(y)
                            the_sum += y+1
                            done = True
                            break
                if done:
                    break
            if done:
                break

        if not done:
            raise 'Problem'
    print(the_sum)


def print_map(a_map):
    for x in range(len(a_map)):
        str_x = str(x)
        if x < 10:
            str_x = f'00{x}'
        elif x < 100:
            str_x = f'0{x}'
        print(f'{str_x}: {a_map[x]}')


if __name__ == "__main__":
    main()
