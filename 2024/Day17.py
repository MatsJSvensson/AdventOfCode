import argparse
import sys
import re
import os, os.path
import math

f = open("input17.txt", "r")
text = f.read()
parts = text.split('\n\n')
registers = parts[0].split('\n')
A = int(registers[0].split(': ')[1])
B = int(registers[1].split(': ')[1])
C = int(registers[2].split(': ')[1])
program_org = parts[1].split(': ')[1]
program_str = program_org.split(',')
program = [int(x) for x in program_str]


def main():
    # First Part
    output = run_program()
    print(output)

    steps = len(program)
    potentials = [0]
    for i in range(steps):
        new_potential = []
        for a in potentials:
            for x in range(8):
                global A
                A = a + x
                output = run_program()
                target = program_org[-(2*i + 1):]
                if output == target:
                    if i == steps - 1:
                        print(f'{a+x} gives: {output}')
                    new_potential.append((a+x)*8)
        potentials = new_potential


def run_program() -> str:
    global A, B, C

    p = 0
    output = ''
    while p + 1 < len(program):
        operation = program[p]
        match operation:
            case 0:
                d = pow(2, combo(program[p + 1]))
                res = A / d
                A = int(res)
            case 1:
                B = B ^ program[p + 1]
            case 2:
                B = combo(program[p + 1]) % 8
            case 3:
                if A != 0:
                    p = program[p + 1]
                    continue
            case 4:
                B = B ^ C
            case 5:
                out = str(combo(program[p + 1]) % 8)
                output += f'{out},'
            case 6:
                d = pow(2, combo(program[p + 1]))
                res = A / d
                B = int(res)
            case 7:
                d = pow(2, combo(program[p + 1]))
                res = A / d
                C = int(res)
            case _:
                print(f'Error: case {program[p]}')
                exit(1)
        p += 2

    if len(output) > 0:
        output = output[:-1]
    return output


def combo(value: int):
    if value < 4:
        return value
    if value == 4:
        return A
    if value == 5:
        return B
    if value == 6:
        return C
    if value > 6:
        print(f'Error: combo {value}')
        exit(1)


def set_point(cave, x, y, char):
    cave[y] = cave[y][:x] + char + cave[y][x+1:]


if __name__ == "__main__":
    main()
