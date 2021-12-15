import argparse
import sys
import re
import os, os.path
import math

def main():
    f = open("input12.txt", "r")
    lines = f.readlines()

    map_dict = {}
    for line in lines:
        if len(line) > 1:
            loc1, loc2 = line.strip().split('-')
            if loc1 in map_dict.keys():
                map_dict[loc1].append(loc2)
            else:
                map_dict[loc1] = []
                map_dict[loc1].append(loc2)
            if loc2 in map_dict.keys():
                map_dict[loc2].append(loc1)
            else:
                map_dict[loc2] = []
                map_dict[loc2].append(loc1)

    paths = find_path(['start'], map_dict)
    for path in paths:
        print(path)

    print(f'sum = {len(paths)}')


def find_path(path, map_dict, small_cave_used=False):
    capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    forbidden = ['start', 'end']
    if path[-1] == 'end':
        return [path]

    paths = []
    for location in map_dict[path[-1]]:
        if location == 'b':
            a = 0
        if location in path and not small_cave_used and location[0] not in capital and location not in forbidden:
            new_path = path.copy()
            new_path.append(location)
            paths.extend(find_path(new_path, map_dict, True))
        elif location not in path or location[0] in capital:
            new_path = path.copy()
            new_path.append(location)
            paths.extend(find_path(new_path, map_dict, small_cave_used))

    return paths


if __name__ == "__main__":
    main()