import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input24.txt", "r")
    text = f.read()
    a_map = text.split('\n')
    length = len(a_map)
    width = len(a_map[0])
    char_map = '.>va<bcd^efghijk'
    x_me = 1
    y_me = 0
    # set_points(a_map, [x_me, y_me], 'S')
    # set_points(a_map, [width-2, length-1], 'X')
    print_map(a_map)
    minutes = 0
    positions = [[x_me, y_me]]
    goals = [[width-2, length-1], [1, 0], [width-2, length-1]]
    goal_count = 0
    for n in range(2001):
        a_map = update_map(a_map, length, width, char_map)
        positions = move(a_map, positions, length)
        if n % 100 == 0:
            set_points(a_map, positions, 'M')
            print(n)
            print_map(a_map)
            set_points(a_map, positions, '.')
        finish = False
        for pos in positions:
            if pos[0] == goals[goal_count][0] and pos[1] == goals[goal_count][1]:
                minutes = n+1
                print(f'Reached goal {goal_count} in {minutes}')
                if goal_count == 2:
                    finish = True
                else:
                    positions = [goals[goal_count]]
                    goal_count += 1
        if finish:
            break

    print(minutes)


def move(a_map, positions, length):
    new_positions = []
    for pos in positions:
        x = pos[0]
        y = pos[1]
        left = a_map[y][x - 1]
        right = a_map[y][x + 1]
        if y == 0:
            up = '-'
        else:
            up = a_map[y - 1][x]
        if y == length-1:
            down = '-'
        else:
            down = a_map[y + 1][x]

        if right == '.':
            add_pos([x+1, y], new_positions)
        if down == '.':
            add_pos([x, y+1], new_positions)
        if a_map[y][x] == '.':
            add_pos([x, y], new_positions)
        if left == '.':
            add_pos([x-1, y], new_positions)
        if up == '.':
            add_pos([x, y-1], new_positions)

    return new_positions


def add_pos(position, positions):
    exist = False
    for pos in positions:
        if pos[0] == position[0] and pos[1] == position[1]:
            exist = True
    if not exist:
        positions.append(position)


def update_map(a_map, length, width, char_map):
    new_map = a_map.copy()
    for y in range(1, length-1):
        for x in range(1, width-1):
            a_sum = 0
            left = a_map[y][x-1]
            if left in '#XS':
                left = a_map[y][width-2]
            if char_map.find(left) % 2 == 1:
                a_sum += 1

            right = a_map[y][x + 1]
            if right in '#XS':
                right = a_map[y][1]
            if char_map.find(right) % 8 > 3:
                a_sum += 4

            up = a_map[y - 1][x]
            if up in '#XS':
                up = a_map[length-2][x]
            if char_map.find(up) % 4 > 1:
                a_sum += 2

            down = a_map[y + 1][x]
            if down in '#XS':
                down = a_map[1][x]
            if char_map.find(down) > 7:
                a_sum += 8

            set_points(new_map, [x, y], char_map[a_sum])
    return new_map


def set_points(a_map, positions, char):
    if not isinstance(positions[0], list):
        positions = [positions]
    for position in positions:
        x = position[0]
        y = position[1]
        a_map[y] = a_map[y][:x] + char + a_map[y][x+1:]


def print_map(a_map):
    for line in a_map:
        print(line)
    print('')


if __name__ == "__main__":
    main()
