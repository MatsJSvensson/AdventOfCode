import argparse
import sys
import re
import os, os.path
import math

f = open("input13.txt", "r")
text = f.read()
pairs = text.split('\n\n')


def main():
    the_sum = 0
    for n in range(len(pairs)):
        left, right = pairs[n].split('\n')
        x = convert(left)
        y = convert(right)
        if compare_lists(x, y) == 1:
            the_sum += n + 1
        pass

    print(the_sum)
    lines = text.replace('\n\n', '\n').split('\n')
    list_of_lists = [convert(lines[0])]
    for line in lines[1:]:
        a_list = convert(line)
        inserted = False
        for n in range(len(list_of_lists)):
            if compare_lists(list_of_lists[n], a_list) == -1:
                list_of_lists.insert(n, a_list)
                inserted = True
                break
        if not inserted:
            list_of_lists.append(a_list)

    divider1 = [[2]]
    divider2 = [[6]]
    index1 = 0
    index2 = 0

    for n in range(len(list_of_lists)):
        if compare_lists(list_of_lists[n], divider1) == -1:
            list_of_lists.insert(n, divider1)
            index1 = n + 1
            break

    for n in range(len(list_of_lists)):
        if compare_lists(list_of_lists[n], divider2) == -1:
            list_of_lists.insert(n, divider2)
            index2 = n + 1
            break

    print(len(lines))
    print(len(list_of_lists))
    print(index1 * index2)


def convert(text):
    length = len(text)
    the_list = []
    in_sub = 0
    number = ''
    for n in range(1, length):
        char = text[n]
        if char == '[':
            if in_sub == 0:
                the_list.append(convert(text[n:]))
            in_sub += 1
        elif char == ']':
            in_sub -= 1
            if in_sub == -1:
                if number != '':
                    the_list.append(int(number))
                return the_list
        elif char in '0123456789' and in_sub == 0:
            number += char
        elif char == ',' and number != '' and in_sub == 0:
            the_list.append(int(number))
            number = ''
        pass


def compare_lists(x, y):
    for n in range(min([len(x), len(y)])):
        if isinstance(x[n], list):
            if isinstance(y[n], list):
                result = compare_lists(x[n], y[n])
                if result != 0:
                    return result
            else:
                result = compare_lists(x[n], [y[n]])
                if result != 0:
                    return result
        elif isinstance(y[n], list):
            result = compare_lists([x[n]], y[n])
            if result != 0:
                return result
        else:
            if x[n] > y[n]:
                return -1
            elif x[n] < y[n]:
                return 1
    if len(x) < len(y):
        return 1
    elif len(x) > len(y):
        return -1
    else:
        return 0


if __name__ == "__main__":
    main()
