import argparse
import sys
import re
import os, os.path

def main():
    f = open("input.txt", "r")
    input = f.read().split('\n')

    result= containBags("shiny gold", input)
    number = bagsContain("shiny gold", input)

    unique = []
    for color in result:
        if color not in unique:
            unique.append(color)

    print(unique)
    print(len(unique))
    print(number)


def containBags(color, list):
    result = []
    for line in list:
        parts = line.split('contain')
        if color in parts[1]:
            color2 = parts[0].replace(" bags ",'')
            result.append(color2)
            result.extend(containBags(color2, list))
    return result

def bagsContain(color, list):
    number = 0
    for line in list:
        parts = line.split('contain')
        subset = parts[1].split(',')
        if color in parts[0]:
            for set in subset:
                if "no other bags" in set:
                    number += 0
                else:
                    splitSet = set.split(' ')
                    color2 = splitSet[2] + ' ' + splitSet[3]
                    contains = bagsContain(color2, list)
                    print(line)
                    print(set)
                    print("{} * {} = {}".format(splitSet[1], contains, int(splitSet[1])*contains))
                    number += int(splitSet[1]) * contains
                    print(number)
    return number + 1






if __name__ == "__main__":
    main()