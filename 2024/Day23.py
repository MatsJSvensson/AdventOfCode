import argparse
import sys
import re
import os, os.path
import math
import aoc_utils as utils
import time

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
                            name = f'{new_list[0]}_{new_list[1]}_{new_list[2]}'
                            if new_list[0] in networks.keys():
                                if name not in networks[new_list[0]]:
                                    networks[new_list[0]].append(name)
                            else:
                                networks[new_list[0]] = [name]

    the_sum = 0
    network_list = []

    for comp in networks.keys():
        for network in networks[comp]:
            if '_t' in network or comp.startswith('t'):
                the_sum += 1
                network_list.append(network)

    network_list.sort()
    print(the_sum)

    networks3 = networks
    networks = {3: networks3}

    # This should be optimized - it takes 20 min to run =)
    for i in range(3, 13):
        the_sum = 0
        name_list = []
        networks[i+1] = {}
        start_time = time.time()
        for comp in networks[i].keys():
            for network in networks[i][comp]:
                clients = network.split('_')
                for c in con_dict[comp]:
                    if c in clients:
                        continue

                    temp_clients = clients + [c]
                    temp_clients.sort()
                    name = '_'.join(temp_clients)
                    if name in name_list:
                        continue
                    else:
                        name_list.append(name)

                    match = True
                    for client in clients[1:]:
                        if c not in con_dict[client]:
                            match = False
                            break
                    if match:
                        if temp_clients[0] not in networks[i + 1].keys():
                            networks[i + 1][temp_clients[0]] = []
                        networks[i+1][temp_clients[0]].append(name)
                        the_sum += 1
        level_time = time.time() - start_time
        print(f'Level {i+1} took {level_time}s seconds to find {the_sum} networks')
        if len(networks[i+1]) == 1:
            print(networks[i+1])
            for key, val in networks[i+1]:
                print(val.replace('_', ','))
            break
    print('end')


if __name__ == "__main__":
    main()
