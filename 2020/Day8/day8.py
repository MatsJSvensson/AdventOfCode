import argparse
import sys
import re
import os, os.path

def main():
    f = open("input.txt", "r")
    input = f.read().split('\n')

    goal = 0
    badest = 0

    for a in range(len(input)):

        done = []
        x = 0
        value = 0
        biggest = 0

        while x > -1:
            line = input[x]
            if a == x:
                if "nop" in line:
                    line = line.replace("nop", "jmp")
                if "jmp" in line:
                    line = line.replace("jmp", "nop")
            if "acc" in line:
                command = line.replace("acc ",'')
                value += int(command)
                x += 1
            if "nop" in line:
                x += 1
            if "jmp" in line:
                command = line.replace("jmp ", '')
                x += int(command)

            if x > biggest:
                biggest = x

            if x in done:
                print("value: {} {}".format(value, biggest))
                break
            elif x >= len(input):
                print("Heureka! Value: {}".format(value))
                goal = value
                break
            else:
                done.append(x)
        if biggest > badest:
            badest = biggest

    print("Heureka! Value: {} {}".format(goal, badest))





if __name__ == "__main__":
    main()