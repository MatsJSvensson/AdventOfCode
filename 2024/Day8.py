import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input8.txt", "r")
    text = f.read()
    a_map = text.split('\n')
    width = len(a_map[0])
    height = len(a_map)
    big_dict = {}
    nodes = {}

    for y in range(height):
        for x in range(width):
            char = a_map[y][x]
            if char != '.':
                if char not in big_dict.keys():
                    big_dict[char] = [[x, y]]
                else:
                    for place in big_dict[char]:
                        x_diff = place[0] - x
                        y_diff = place[1] - y
                        node1 = [place[0] + x_diff, place[1] + y_diff]
                        node2 = [x - x_diff, y - y_diff]
                        if check_node(node1, width, height):
                            n1 = f'{node1[0]}_{node1[1]}'
                            if n1 in nodes.keys():
                                nodes[n1] += 1
                            else:
                                nodes[n1] = 1
                        if check_node(node2, width, height):
                            n2 = f'{node2[0]}_{node2[1]}'
                            if n2 in nodes.keys():
                                nodes[n2] += 1
                            else:
                                nodes[n2] = 1

                    big_dict[char].append([x, y])

    print(f'sum: {len(nodes.keys())}')

    big_dict = {}
    nodes = {}

    for y in range(height):
        for x in range(width):
            char = a_map[y][x]
            if char != '.':
                if char not in big_dict.keys():
                    big_dict[char] = [[x, y]]
                else:
                    for place in big_dict[char]:
                        x_diff = place[0] - x
                        y_diff = place[1] - y
                        for t in range(100):
                            node1 = [place[0] + x_diff * t, place[1] + y_diff * t]
                            if check_node(node1, width, height):
                                n1 = f'{node1[0]}_{node1[1]}'
                                if n1 in nodes.keys():
                                    nodes[n1] += 1
                                else:
                                    nodes[n1] = 1
                            else:
                                break
                        for t in range(100):
                            node2 = [x - x_diff * t, y - y_diff * t]
                            if check_node(node2, width, height):
                                n2 = f'{node2[0]}_{node2[1]}'
                                if n2 in nodes.keys():
                                    nodes[n2] += 1
                                else:
                                    nodes[n2] = 1
                            else:
                                break

                    big_dict[char].append([x, y])

    print(f'sum: {len(nodes.keys())}')


def check_node(node, width, height):
    result = True
    if node[0] < 0 or node[0] > width - 1:
        result = False
    if node[1] < 0 or node[1] > height - 1:
        result = False
    return result


if __name__ == "__main__":
    main()
