import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input10.txt", "r")
    text = f.read()
    the_map = text.split('\n')
    map_copy = the_map.copy()
    start = []
    for y in range(len(the_map)):
        line = the_map[y]
        if 'S' in line:
            start = [line.find('S'), y]

    sys.setrecursionlimit(100000)
    path = {f'{start[0]}_{start[1]}': 'E'}
    length = find_next(start[0]+1, start[1], 'E', 'N', the_map, path)
    #length = find_next(start[0], start[1]+1, 'S', 'W', the_map, path)
    print(length/2)

    sys.setrecursionlimit(1000)
    inside_points = []
    count_inside(path, inside_points)
    num_inside = len(inside_points)
    print(num_inside)

    for y in range(len(the_map)):
        for x in range(len(the_map[0])):
            point = f'{x}_{y}'
            if point in inside_points:
                the_map[y] = the_map[y][:x] + '*' + the_map[y][x + 1:]
            elif point in path.keys():
                #the_map[y] = the_map[y][:x] + '#' + the_map[y][x + 1:]
                pass
            else: #if the_map[y][x] != '.':
                the_map[y] = the_map[y][:x] + ' ' + the_map[y][x + 1:]

    print()
    for x in range(len(the_map)):
        str_x = str(x)
        if x < 10:
            str_x = f'00{x}'
        if x < 100:
            str_x = f'0{x}'
        print(f'{str_x}: {the_map[x]}')


def count_inside(path, inside_points):
    for point in path.keys():
        x, y = point.split('_')
        new_x = int(x)
        new_y = int(y)
        if path[point] == 'E':
            new_x += 1
        if path[point] == 'W':
            new_x -= 1
        if path[point] == 'S':
            new_y += 1
        if path[point] == 'N':
            new_y -= 1
        propagate(new_x, new_y, path.keys(), inside_points)


def propagate(x, y, path_keys, inside_points):
    if not (0 <= x <= 140) or not (0 <= y <= 140):
        raise 'problem'
    if f'{x}_{y}' in path_keys or f'{x}_{y}' in inside_points:
        pass
    else:
        inside_points.append(f'{x}_{y}')
        propagate(x+1, y, path_keys, inside_points)
        propagate(x-1, y, path_keys, inside_points)
        propagate(x, y+1, path_keys, inside_points)
        propagate(x, y-1, path_keys, inside_points)


def find_next(x, y, dir, inside, the_map, path):
    char = the_map[y][x]
    new_inside = inside
    if char == 'J':
        if dir == 'S':
            new_dir = 'W'
        elif dir == 'E':
            new_dir = 'N'
        else:
            new_dir = '0'
        if inside == 'E':
            new_inside = 'S'
        elif inside == 'S':
            new_inside = 'E'
        elif inside == 'N':
            new_inside = 'W'
        elif inside == 'W':
            new_inside = 'N'
    elif char == 'L':
        if dir == 'S':
            new_dir = 'E'
        elif dir == 'W':
            new_dir = 'N'
        else:
            new_dir = '0'
        if inside == 'E':
            new_inside = 'N'
        elif inside == 'N':
            new_inside = 'E'
        elif inside == 'S':
            new_inside = 'W'
        elif inside == 'W':
            new_inside = 'S'
    elif char == 'F':
        if dir == 'N':
            new_dir = 'E'
        elif dir == 'W':
            new_dir = 'S'
        else:
            new_dir = '0'
        if inside == 'E':
            new_inside = 'S'
        elif inside == 'S':
            new_inside = 'E'
        elif inside == 'N':
            new_inside = 'W'
        elif inside == 'W':
            new_inside = 'N'
    elif char == '7':
        if dir == 'N':
            new_dir = 'W'
        elif dir == 'E':
            new_dir = 'S'
        else:
            new_dir = '0'
        if inside == 'E':
            new_inside = 'N'
        elif inside == 'N':
            new_inside = 'E'
        elif inside == 'S':
            new_inside = 'W'
        elif inside == 'W':
            new_inside = 'S'
    elif char == '-':
        if dir in 'EW':
            new_dir = dir
        else:
            new_dir = '0'
    elif char == '|':
        if dir in 'NS':
            new_dir = dir
        else:
            new_dir = '0'
    else:
        new_dir = '0'

    if new_dir == '0':
        raise f'Error at {x},{y} {char}'

    if new_dir == 'W':
        new_x = x - 1
        new_y = y
    elif new_dir == 'E':
        new_x = x + 1
        new_y = y
    elif new_dir == 'N':
        new_x = x
        new_y = y - 1
    elif new_dir == 'S':
        new_x = x
        new_y = y + 1
    else:
        raise f'Error2 at {x},{y} {char}'

    path[f'{x}_{y}'] = inside

    if the_map[new_y][new_x] == 'S':
        return 1
    else:
        return find_next(new_x, new_y, new_dir, new_inside, the_map, path) + 1

def other():
    P="input10.txt"
    with open(P,"r") as f:
        R=f.read()
    G=R.split("\n")
    H=len(G)
    W=len(G[0])

    O = [[0]*W for _ in range(H)] # part 2

    ax = -1
    ay = -1
    for i in range(H):
        for j in range(W):
            if "S" in G[i]:
                ax=i
                ay=G[i].find("S")
    print(ax,ay)

    # rightward downward leftward upward
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    happy = ["-7J", "|LJ", "-FL", "|F7"]
    Sdirs = []
    for i in range(4):
        pos = dirs[i]
        bx = ax+pos[0]
        by = ay+pos[1]
        if bx>=0 and bx<=H and by>=0 and by<=W and G[bx][by] in happy[i]:
            Sdirs.append(i)
    print(Sdirs)
    Svalid = 3 in Sdirs # part 2

    # rightward downward leftward upward
    transform = {
        (0,"-"): 0,
        (0,"7"): 1,
        (0,"J"): 3,
        (2,"-"): 2,
        (2,"F"): 1,
        (2,"L"): 3,
        (1,"|"): 1,
        (1,"L"): 0,
        (1,"J"): 2,
        (3,"|"): 3,
        (3,"F"): 0,
        (3,"7"): 2,
    }

    curdir = Sdirs[0]
    cx = ax + dirs[curdir][0]
    cy = ay + dirs[curdir][1]
    ln = 1
    O[ax][ay] = 1 # Part 2
    while (cx,cy)!=(ax,ay):
        O[cx][cy] = 1 # Part 2
        ln += 1
        curdir = transform[(curdir,G[cx][cy])]
        cx = cx + dirs[curdir][0]
        cy = cy + dirs[curdir][1]
    print(ln)
    print(ln//2)

    # End Part 1
    # Begin Part 2

    ct = 0
    for i in range(H):
        inn = False
        for j in range(W):
            if O[i][j]:
                if G[i][j] in "|JL" or (G[i][j]=="S" and Svalid): inn = not inn
            else:
                ct += inn
    print(ct)

if __name__ == "__main__":
    main()
    other()
