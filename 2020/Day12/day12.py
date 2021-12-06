import argparse
import sys
import re
import os, os.path

def main():
    f = open("input.txt", "r")
    input = f.read().split('\n')

    coord = [0,0]
    waypoint = [10,1]


    dirs = [[1,0],[0,1],[-1,0],[0,-1]]
    dir = 0

    print("{} {} {}".format('-', coord, waypoint))

    for instr in input:
        if 'N' in instr:
            num = instr.replace('N','')
            waypoint[1] += int(num)
        elif 'S' in instr:
            num = instr.replace('S','')
            waypoint[1] -= int(num)
        elif 'E' in instr:
            num = instr.replace('E','')
            waypoint[0] += int(num)
        elif 'W' in instr:
            num = instr.replace('W','')
            waypoint[0] -= int(num)
        elif '180' in instr:
            waypoint[0] *= -1
            waypoint[1] *= -1
        elif 'L90' in instr or 'R270' in instr:
            temp0 = -waypoint[1]
            waypoint[1] = waypoint[0]
            waypoint[0] = temp0
        elif 'R90' in instr or 'L270' in instr:
            temp0 = waypoint[1]
            waypoint[1] = -waypoint[0]
            waypoint[0] = temp0
        elif 'F' in instr:
            num = int(instr.replace('F', ''))
            coord[0] += waypoint[0]*num
            coord[1] += waypoint[1]*num
        else:
            exit(1)
        print("{} {} {}".format(instr, coord, waypoint))
    print(abs(coord[0]) + abs(coord[1]))






if __name__ == "__main__":
    main()