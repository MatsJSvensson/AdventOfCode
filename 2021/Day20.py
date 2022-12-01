import argparse
import sys
import re
import os, os.path
import math

def main():
    f = open("input20.txt", "r")
    enhancer, picture = f.read().split('\n\n')
    picture = picture.split('\n')

    height = len(picture)
    length = len(picture[0])
    padding = 100
    repetitions = 50

    picture = expand_picture(picture, padding)

    # for line in picture:
    #     print(line)

    for n in range(repetitions):
        picture = enhance_picture(picture,enhancer)
        print(n)
        # for line in picture:
        #     print(line)

    the_sum = 0
    discounts = padding - repetitions
    for line in picture[discounts:len(picture)-discounts]:
        the_sum += line[discounts:len(picture[0])-discounts].count('#')
    print(the_sum)


def empty_row(n):
    string = ''
    for n in range(n):
        string += '.'
    return string


def expand_picture(picture, n=1):
    for x in range(n):
        length = len(picture[0])
        new_picture = []
        new_picture.append(empty_row(length + 2))
        for row in picture:
            new_picture.append('.' + row + '.')
        new_picture.append(empty_row(length + 2))
        picture = new_picture.copy()
    return picture


def enhance_picture(picture, enhancer):
    height = len(picture)
    length = len(picture[0])
    new_picture = [empty_row(length)]

    for y in range(1,height-1):
        line = '.'
        for x in range(1, length-1):
            binary = ''
            for j in range(y-1,y+2):
                for i in range(x-1,x+2):
                    if picture[j][i] == '#':
                        binary += '1'
                    elif picture[j][i] == '.':
                        binary += '0'
                    else:
                        print('Error')
                        exit(1)
            integer = int(binary, 2)
            line += enhancer[integer]
        line += '.'
        new_picture.append(line)
    new_picture.append(empty_row(length))
    return new_picture






if __name__ == "__main__":
    main()