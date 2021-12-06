import argparse
import sys
import re
import os, os.path

def main():
    parser = argparse.ArgumentParser(description='Day 1')
    parser.add_argument('--expenseList', required=True)

    args = parser.parse_args()
    input = args.expenseList
    eList = input.split(',')
    eList.sort()
    a = 0
    for x in eList:
        for y in eList[a:]:
            b = a
            if int(x) + int(y) == 2020:
                print("Product {}*{} = {}".format(x, y, int(x)*int(y)))
            for z in eList[b:]:
                if int(x) + int(y) + int(z) == 2020:
                    print("Product {}*{}*{} = {}".format(x, y, z, int(x) * int(y) * int(z)))
            b = b+1
        a = a+1

if __name__ == "__main__":
    main()