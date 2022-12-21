import argparse
import sys
import re
import os, os.path


def main():
    f = open("input8.txt", "r")
    lines = f.read().split('\n')
    counter = 0
    highest_score = 0
    highest_x = -1
    highest_y = -1

    for X in range(len(lines)):
        for Y in range(len(lines[0])):
            height = lines[Y][X]
            if (check_tree(lines, X, Y, height, [0, 1]) or check_tree(lines, X, Y, height, [0, -1])
                    or check_tree(lines, X, Y, height, [1, 0]) or check_tree(lines, X, Y, height, [-1, 0])):
                counter += 1
            factor1 = check_tree2(lines, X, Y, height, [0, 1], 0)
            factor2 = check_tree2(lines, X, Y, height, [0, -1], 0)
            factor3 = check_tree2(lines, X, Y, height, [1, 0], 0)
            factor4 = check_tree2(lines, X, Y, height, [-1, 0], 0)
            scenic_score = factor1 * factor2 * factor3 * factor4
            if scenic_score > highest_score:
                highest_score = scenic_score
                highest_x = X
                highest_y = Y

    print(counter)
    print("{},{}: {}".format(highest_x, highest_y, highest_score))


def check_tree(lines, x, y, height, dir):
    new_x = x + dir[0]
    new_y = y + dir[1]
    if new_y == len(lines) or new_x == len(lines[0]) or new_x == -1 or new_y == -1:
        return True
    if height > lines[new_y][new_x]:
        return check_tree(lines, new_x, new_y, height, dir)
    else:
        return False


def check_tree2(lines, x, y, height, dir, counter):
    counter += 1
    new_x = x + dir[0]
    new_y = y + dir[1]
    if new_y == len(lines) or new_x == len(lines[0]) or new_x == -1 or new_y == -1:
        return counter - 1
    if height > lines[new_y][new_x]:
        return check_tree2(lines, new_x, new_y, height, dir, counter)
    else:
        return counter


if __name__ == "__main__":
    main()
