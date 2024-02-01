import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("C:/temp/sews.a2l", "r")
    text = f.read()

    pattern = 'Rte_Address_([A-Z0-9]{5})_([A-Z0-9]{5})'
    matches = re.finditer(pattern, text)
    for match in matches:
        if match.group(1) != match.group(2):
            print(f'{match.group(1)} {match.group(2)}')


if __name__ == "__main__":
    main()
