import argparse
import sys
import re
import os, os.path


def main():
    f = open("input6.txt", "r")
    text = f.read()
    parts = text.split('\n')
    times = parts[0].split(': ')[1].split('     ')
    distances = parts[1].split(': ')[1].split('   ')
    product = 1
    for x in range(len(times)):
        time = int(times[x])
        distance = int(distances[x])
        a_sum = 0
        for y in range(time):
            length = (time - y) * y
            if length > distance:
                a_sum += 1
        product *= a_sum
        print(f'{a_sum} {product}')

    time = 45977295
    distance = 305106211101695
    the_sum = 0
    for y in range(time):
        length = (time - y) * y
        if length > distance:
            the_sum += 1
    print(the_sum)


if __name__ == "__main__":
    main()
