import argparse
import math
import sys
import re
import os, os.path


def main():
    f = open("input5.txt", "r")
    text = f.read()
    parts = text.split('\n\n')
    rules = parts[0].split('\n')
    updates = parts[1].split('\n')
    the_sum = 0
    sum2 = 0

    for update in updates:
        pages = update.split(',')
        valid = validate(pages, rules)

        if valid:
            length = len(pages)
            index = int(math.floor(length/2))
            the_sum += int(pages[index])
        else:
            new_pages = pages.copy()
            for rule in rules:
                page1, page2 = rule.split('|')
                if page1 in pages and page2 in new_pages:
                    index1 = new_pages.index(page1)
                    index2 = new_pages.index(page2)
                    if index1 > index2:
                        new_pages.pop(index1)
                        new_pages.insert(index2, page1)
            for rule in rules:
                page1, page2 = rule.split('|')
                if page1 in pages and page2 in new_pages:
                    index1 = new_pages.index(page1)
                    index2 = new_pages.index(page2)
                    if index1 > index2:
                        new_pages.pop(index1)
                        new_pages.insert(index2, page1)
            valid = validate(new_pages, rules)
            if valid:
                length = len(pages)
                index = int(math.floor(length / 2))
                sum2 += int(new_pages[index])
            else:
                print(pages)

    print(f'Sum: {the_sum}')
    print(f'Sum2: {sum2}')


def validate(pages, rules):
    valid = True
    for rule in rules:
        page1, page2 = rule.split('|')
        if page1 in pages and page2 in pages:
            index1 = pages.index(page1)
            index2 = pages.index(page2)
            if index1 > index2:
                valid = False
                break
    return valid


if __name__ == "__main__":
    main()
