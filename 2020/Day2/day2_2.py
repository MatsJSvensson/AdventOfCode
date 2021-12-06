import argparse
import sys
import re
import os, os.path

def main():
    f = open("input2.txt", "r")
    input = f.read().split('\n')
    invalids = 0
    total = 0
    for line in input:
        #print(line)
        check = 0
        splitLine = line.split(':')
        policy = splitLine[0]
        password = splitLine[1]
        splitPolicy = policy.split(' ')
        character = splitPolicy[1]
        indexes = splitPolicy[0].split('-')
        if password[int(indexes[0])] is character:
            print("{} is {}".format(password[int(indexes[0]) - 1],character))
            check = check+1
        if password[int(indexes[1])] is character:
            check = check+1
        if check != 1:
            print("Invalid pass: {}".format(line))
            print("{} not in place {} xor {}".format(character,indexes[0],indexes[1]))
            print("indexes and check: {} {} {}".format(indexes[0],indexes[1], check))
            invalids = invalids+1
        total = total+1
    print("Valid passwords: {}".format(total - invalids))



if __name__ == "__main__":
    main()