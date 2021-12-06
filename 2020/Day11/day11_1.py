import argparse
import sys
import re
import os, os.path

def main():
    f = open("input.txt", "r")
    input = f.read().split('\n')

    width = len(input[0])+2
    top = ''
    bottom = ''
    chairs = []

    for x in range(width):
        top += '.'
        bottom += '.'

    chairs.append(top)
    for line in input:
        line = '.' + line + '.'
        chairs.append(line)
    chairs.append(bottom)
    chairs_new = chairs.copy()

    change = True
    seated = 0
    while(change):
        change = False
        seated = 0
        for y in range(1,len(input)+1):
            for x in range(1,width):
                up = chairs[y][x-1:x+2].count('#')
                mi = chairs[y-1][x-1:x+2].count('#')
                lo = chairs[y+1][x-1:x+2].count('#')
                tot = up + mi + lo

                if chairs[y][x] is 'L' and tot < 1:
                    chairs_new[y] = chairs_new[y][:x] + '#' + chairs_new[y][x+1:]
                    change = True
                elif chairs[y][x] is '#' and tot >= 5:
                    chairs_new[y] = chairs_new[y][:x] + 'L' + chairs_new[y][x+1:]
                    change = True
            seated += chairs_new[y].count('#')
            print(chairs_new[y])
        print("Seated: {}".format(seated))
        chairs = chairs_new.copy()


if __name__ == "__main__":
    main()