import argparse
import sys
import re
import os, os.path

def main():
    f = open("input.txt", "r")
    input = f.read().split('\n\n')

    sum = 0
    for group in input:
        persons = group.split('\n')
        chars = "abcdefghijklmnopqrstuvwxyz"
        for person in persons:
            for char in chars:
                if char not in person:
                    chars = chars.replace(char,'')
                    print(chars)
        nChars = len(chars)
        print("Answers: {} Sum: {}".format(chars,nChars))
        sum += nChars

    print("Sum: {} ".format(sum))




if __name__ == "__main__":
    main()