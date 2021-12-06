import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input.txt", "r")
    input = f.read().split('\n')

    blacks = []

    for row in input:
        x = 0
        y = 0
        i = 0
        while i < len(row):
            if row[i] is 'n' or row[i] is 's':
                dir = row[i:i+2]
                i += 1
            else:
                dir = row[i]
            if 's' in dir:
                y -= 1
                if 'e' in dir:
                    x += 1
            elif 'n' in dir:
                y += 1
                if 'w' in dir:
                    x -= 1
            elif 'w' in dir:
                x -= 1
            elif 'e' in dir:
                x += 1
            else:
                exit(1000)
            i += 1
        coord = [x, y]
        if coord in blacks:
            blacks.remove(coord)
        else:
            blacks.append(coord)

    blackDict = {}
    for coord in blacks:
        x = coord[0]
        y = coord[1]
        name = str(x) + ' ' + str(y)
        blackDict[name] = surrounders(x,y)


    for i in range(100):
        print(i)
        whites = {}
        greys = {}
        for black in blackDict.keys():
            counter = 0
            for coord in blackDict[black]:
                name = str(coord[0]) + ' ' + str(coord[1])
                try:
                    if blackDict[name]:
                        counter += 1
                except:
                    whites[name] = True
            if counter == 0 or counter > 2:
                greys[black] = True

        toBlack = {}
        for white in whites.keys():
            x = int(white.split()[0])
            y = int(white.split()[1])
            counter = 0
            coords = surrounders(x,y)
            for coord in coords:
                name = str(coord[0]) + ' ' + str(coord[1])
                try:
                    if blackDict[name]:
                        counter += 1
                except:
                    hej = 1
            if counter == 2:
                toBlack[white] = coords

        for black in toBlack.keys():
            blackDict[black] = toBlack[black]

        for grey in greys.keys():
            blackDict.pop(grey)


    print(len(blackDict))

def surrounders(x,y):
    result = []
    result.append([x+1,y])
    result.append([x,y+1])
    result.append([x+1,y-1])
    result.append([x-1,y])
    result.append([x,y-1])
    result.append([x-1,y+1])
    return result



    print(len(blacks))

if __name__ == "__main__":
    main()