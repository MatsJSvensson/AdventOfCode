import argparse
import sys
import re
import os, os.path

def main():
    f = open("input.txt", "r")
    input = f.read().split('\n\n')

    emptyLine = True
    valid = 0
    for instance in input:

        if (instance.find('iyr:') >= 0 and instance.find('eyr:') >= 0 and instance.find('hcl:') >= 0 and instance.find('hgt:') >= 0):
            #print("found: {}".format(instance.find("byr:")))
            if(instance.find('ecl:') >= 0 and instance.find('pid:') >= 0 and instance.find("byr:") >= 0):
                print("Found")
                print(instance)
                valid += 1
    print("Valid: {}".format(valid))




if __name__ == "__main__":
    main()