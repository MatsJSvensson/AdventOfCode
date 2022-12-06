import argparse
import sys
import re
import os, os.path


def main():
    f = open("input6.txt", "r")
    stream = f.read().split('\n')[0]
    substream = '    '
    counter = 0
    for char in stream:
        counter += 1
        substream = substream[1:]
        substream += char
        found = False
        for part in substream:
            if substream.count(part) >= 2:
                found = True

        if not found and counter >= 4:
            break

    print('counter: {}'.format(counter))
    counter = 0
    substream = '              '
    for char in stream:
        counter += 1
        substream = substream[1:]
        substream += char
        found = False
        for part in substream:
            if substream.count(part) >= 2:
                found = True

        if not found and counter >= 14:
            break

    print('counter: {}'.format(counter))


if __name__ == "__main__":
    main()
