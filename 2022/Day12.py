import argparse
import sys
import re
import os, os.path
import math

f = open("input12.txt", "r")
lines = f.read().split('\n')
max_x = len(lines[0])
max_y = len(lines)
alfabet = 'abcdefghijklmnopqrstuvwxyz'


def main():
    visited = {}
    max_path = 450
    pathfinder([0, 20], visited, 0, max_path)
    print(visited['E'])
    visited.clear()
    path_lengths = {}

    for x in range(max_x):
        for y in range(max_y):
            if lines[y][x] == 'a':
                pathfinder([x, y], visited, 0, max_path)
                if 'E' in visited.keys():
                    if visited['E'] < max_path:
                        path_lengths[f'{x} {y}'] = visited['E']
                        max_path = visited['E']
    print(path_lengths)


def pathfinder(coord, visited, path_length, max_path):
    if 'E' in visited.keys():
        if path_length > visited['E']:
            return
    if path_length > max_path:
        return
    x = coord[0]
    y = coord[1]
    if f'{x} {y}' in visited.keys():
        if path_length >= visited[f'{x} {y}']:
            return
    visited[f'{x} {y}'] = path_length
    # print(f'{x} {y}: {path_length}')
    current_char = lines[coord[1]][coord[0]]
    current_elevation = alfabet.find(current_char)
    new_coords = []
    if x + 1 < max_x:
        new_coords.append([x+1, y])
    if x - 1 >= 0:
        new_coords.append([x-1, y])
    if y + 1 < max_y:
        new_coords.append([x, y+1])
    if y - 1 >= 0:
        new_coords.append([x, y-1])

    for dest in new_coords:
        new = lines[dest[1]][dest[0]]
        if new == 'E' and current_char in 'yz':
            print(f'path_length: {path_length}')
            if 'E' in visited.keys():
                if path_length + 1 < visited['E']:
                    visited['E'] = path_length + 1
            else:
                visited['E'] = path_length + 1
            break
        if alfabet.find(new) - current_elevation <= 1:
            pathfinder(dest, visited, path_length + 1, max_path)


if __name__ == "__main__":
    main()
