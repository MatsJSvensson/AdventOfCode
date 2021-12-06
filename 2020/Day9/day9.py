import argparse
import sys
import re
import os, os.path

def main():
    f = open("input.txt", "r")
    input = f.read().split('\n')

    the25 = []
    missing = 0

    for line in input:
        num = int(line)
        if len(the25) >= 25:
            found = False
            for x in range(0,25):
                for y in range(x+1,25):
                    if the25[x] + the25[y] == num:
                        found = True
                        print("{} + {} = {}".format(the25[x], the25[y], num))
                        break
                if found:
                    break
            if not found:
                print("FIRST MISSING SUM: {}".format(num))
                if missing == 0:
                    missing = num
            the25.pop(0)
        the25.append(num)


    print("Missing: {} ".format(missing))

    theX = -1
    theY = -1
    x = 0
    for line in input:
        y = x+1
        sum = int(line)
        for line in input[x+1:]:
            sum += int(line)
            if sum == missing:
                print("Heureka! Lines: {} {}".format(x,y))
                if theX == -1:
                    theX = x
                    theY = y
                break
            if sum > missing:
                break
            y += 1

        x += 1

    smallest = missing
    largest = 0
    for line in input[theX:theY]:
        if int(line) < smallest:
            smallest = int(line)
        if int(line) > largest:
            largest = int(line)

    print("{} + {} = {}".format(largest,smallest,largest+smallest))





if __name__ == "__main__":
    main()