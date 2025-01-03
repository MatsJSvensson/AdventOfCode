import argparse
import sys
import re
import os, os.path
import math
import aoc_utils as utils

f = open("input23.txt", "r")
text = f.read()
connections = text.split('\n')
con_dict ={}

for connection in connections:
    a, b = connection.split('-')
    if a in con_dict.keys():
        if b not in con_dict[a]:
            con_dict[a].append(b)
    else:
        con_dict[a] = [b]
    if b in con_dict.keys():
        if a not in con_dict[b]:
            con_dict[b].append(a)
    else:
        con_dict[b] = [a]


def main():
    networks = {}
    for comp in con_dict.keys():
        if len(con_dict[comp]) > 1:
            for c1 in con_dict[comp]:
                for c2 in con_dict[comp]:
                    if c1 != c2:
                        if c1 in con_dict[c2]:
                            new_list = [comp, c1, c2]
                            new_list.sort()
                            name = f'_{new_list[0]}_{new_list[1]}_{new_list[2]}'
                            if new_list[0] in networks.keys():
                                if name not in networks[new_list[0]]:
                                    networks[new_list[0]].append(name)
                            else:
                                networks[new_list[0]] = [name]

    the_sum = 0
    network_list = []

    for comp in networks.keys():
        for network in networks[comp]:
            if '_t' in network:
                the_sum += 1
                network_list.append(network)

    network_list.sort()
    print(the_sum)


if __name__ == "__main__":
    main()
