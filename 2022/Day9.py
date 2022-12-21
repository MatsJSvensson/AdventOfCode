import argparse
import sys
import re
import os, os.path


def main():
    f = open("input9.txt", "r")
    lines = f.read().split('\n')

    head = [0, 0]
    tail = [0, 0]
    pos_list = []

    for line in lines:
        char, dist = line.split(' ')
        dir = [0, 0]
        if char == 'D':
            dir = [0, -1]
        elif char == 'R':
            dir = [1, 0]
        elif char == 'U':
            dir = [0, 1]
        elif char == 'L':
            dir = [-1, 0]
        else:
            print('ERROR')

        for n in range(int(dist)):
            head[0] += dir[0]
            head[1] += dir[1]
            diff_x = head[0] - tail[0]
            diff_y = head[1] - tail[1]
            if abs(diff_x) > 1:
                tail[0] += diff_x / abs(diff_x)
                if abs(diff_y) > 0:
                    tail[1] += diff_y / abs(diff_y)
            elif abs(diff_y) > 1:
                tail[1] += diff_y/abs(diff_y)
                if abs(diff_x) > 0:
                    tail[0] += diff_x / abs(diff_x)

            string_rep = "{} {}".format(tail[0], tail[1])
            if string_rep not in pos_list:
                pos_list.append(string_rep)

    print(len(pos_list))

    knots = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    pos_list2 = []

    for line in lines:
        char, dist = line.split(' ')
        dir = [0, 0]
        if char == 'D':
            dir = [0, -1]
        elif char == 'R':
            dir = [1, 0]
        elif char == 'U':
            dir = [0, 1]
        elif char == 'L':
            dir = [-1, 0]
        else:
            print('ERROR')

        for n in range(int(dist)):
            knots[0][0] += dir[0]
            knots[0][1] += dir[1]
            for x in range(1, 10):
                diff_x = knots[x-1][0] - knots[x][0]
                diff_y = knots[x-1][1] - knots[x][1]
                if abs(diff_x) > 1:
                    knots[x][0] += diff_x / abs(diff_x)
                    if abs(diff_y) > 0:
                        knots[x][1] += diff_y / abs(diff_y)
                elif abs(diff_y) > 1:
                    knots[x][1] += diff_y / abs(diff_y)
                    if abs(diff_x) > 0:
                        knots[x][0] += diff_x / abs(diff_x)

            string_rep = "{} {}".format(knots[9][0], knots[9][1])
            if string_rep not in pos_list2:
                pos_list2.append(string_rep)
    print(len(pos_list2))


if __name__ == "__main__":
    main()
