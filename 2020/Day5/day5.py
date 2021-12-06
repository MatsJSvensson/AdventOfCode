import argparse
import sys
import re
import os, os.path

def main():
    f = open("input.txt", "r")
    input = f.read().split('\n')
    highest = 0
    lowest = 900
    x = 7
    answer = 6

    for boarding in input:
        answer += x
        x += 1
        row = 0
        column = 0
        counter = 7
        for char in boarding[0:7]:
            counter -= 1
            if char is 'B':
                row += pow(2,counter)

        counter = 3
        for char in boarding[7:10]:
            counter -= 1
            if char is 'R':
                column += pow(2, counter)
        seat = row*8 + column
        print("Row: {} Column: {} Seat: {}".format(row,column,seat))
        if seat > highest:
            highest = seat
        if seat < lowest:
            lowest = seat
        answer -= seat


    print("Highest: {} Lowest: {} Answer: {} x = {}".format(highest,lowest, answer, x))




if __name__ == "__main__":
    main()