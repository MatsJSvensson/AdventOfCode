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
    free = False
    id = 0
    for char in data:
        num = int(char)
        if free:
            for t in range(num):
                memory.append(-1)
            free = False
        else:
            for t in range(num):
                memory.append(id)
            id += 1
            free = True

    for t in range(len(memory)):
        if t > len(memory) - 1:
            break
        if memory[t] == -1:
            id, memory = get_last(memory)
            if id == -1 or t > len(memory) - 1:
                break
            else:
                memory[t] = id

    for t in range(len(memory)):
        checksum += t * memory[t]

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
