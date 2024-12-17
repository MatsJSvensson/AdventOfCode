import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input9.txt", "r")
    text = f.read()
    data = text.split('\n')[0]
    checksum = 0

    memory = []
    memory_dict = {}
    free_dict = {}
    free = False
    pos = 0
    id = 0
    for char in data:
        num = int(char)
        if free:
            free_dict[id] = [pos, num]
            free = False
        else:
            memory_dict[id] = [pos, num]
            id += 1
            free = True
        pos += num

    for t in range(id):
        x = id - t
        if x not in memory_dict.keys():
            continue
        length = memory_dict[x][1]
        for p in range(1, id):
            if p in free_dict.keys():
                if free_dict[p][1] > 0 and memory_dict[x][0] < free_dict[p][0]:
                    break
                if length <= free_dict[p][1]:
                    memory_dict[x][0] = free_dict[p][0]
                    free_dict[p][1] -= length
                    if free_dict[p][1] == 0:
                        free_dict.pop(p)
                    else:
                        free_dict[p][0] += length
                    break

    for t in range(id):
        for u in range(memory_dict[t][0], memory_dict[t][0] + memory_dict[t][1]):
            checksum += t * u

    print(f'checksum: {checksum}')


def get_last(memory):
    mem = memory.copy()
    mem.reverse()
    for m in mem:
        if m != -1:
            memory.pop(-1)
            return m, memory
        else:
            memory.pop(-1)
    return -1, memory


if __name__ == "__main__":
    main()
