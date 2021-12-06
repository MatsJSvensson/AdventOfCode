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
        splitLine = line.split(':')
        policy = splitLine[0]
        password = splitLine[1]
        splitPolicy = policy.split(' ')
        character = splitPolicy[1]
        limits = splitPolicy[0].split('-')
        count = password.count(character)
        if count < int(limits[0]) or count > int(limits[1]):
            print("Invalid pass: {}".format(line))
            print("{} not between {} and {} {}".format(count,limits[0],limits[1],character))
            invalids = invalids+1
        total = total+1
    print("Valid passwords: {}".format(total - invalids))



if __name__ == "__main__":
    main()