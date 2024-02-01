import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input8.txt", "r")
    text = f.read()
    instructions, a_map = text.split('\n\n')
    the_map = {}
    the_sum = 0
    starts = []
    ends = []

    for line in a_map.split('\n'):
        start, goals = line.split(' = (')
        L, R = goals.split(', ')
        R = R.replace(')', '')
        the_map[start] = {'L': L, 'R': R}
        if start[2] == 'A':
            starts.append(start)
        if start[2] == 'Z':
            ends.append(start)
    #
    # place = 'AAA'
    # for x in range(1000000):
    #     pos = x % len(instructions)
    #     dir = instructions[pos]
    #     place = the_map[place][dir]
    #     the_sum += 1
    #     if place == 'ZZZ':
    #         break
    #
    # print(the_sum)

    the_sum = 0
    places = starts
    memory = [{}, {}, {}, {}, {}, {}]
    ins_len = len(instructions)
    for x in range(100000):
        pos = x % ins_len
        dir = instructions[pos]
        goals = 0
        for y in range(len(places)):
            place = the_map[places[y]][dir]
            if place[2] == 'Z':
                goals += 1
                if place in memory[y].keys():
                    if pos in memory[y][place].keys():
                        if 'x2' not in memory[y][place][pos].keys():
                            memory[y][place][pos]['x2'] = x+1
                            memory[y][place][pos]['cycle_len'] = x+1 - memory[y][place][pos]['x1']
                else:
                    memory[y][place] = {pos: {'x1': x+1}}
            places[y] = place

        the_sum += 1
        if goals == len(places):
            break

    print(the_sum)
    product = 1
    cycles = []
    for x in range(len(memory)):
        place = list(memory[x].keys())[0]
        pos = list(memory[x][place].keys())[0]
        cycle_len = memory[x][place][pos]['cycle_len']
        x1 = memory[x][place][pos]['x1']
        x2 = memory[x][place][pos]['x2']
        product *= cycle_len
        print(f'{x1} {x2} {cycle_len}')
        cycles.append(cycle_len)
    print(product)
    print(math.lcm(*cycles))


if __name__ == "__main__":
    main()
