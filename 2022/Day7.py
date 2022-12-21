import argparse
import sys
import re
import os, os.path


def main():
    f = open("input7.txt", "r")
    lines = f.read().split('\n')
    the_list = []
    folder_size(lines, the_list)
    print(the_list)

    size = 0
    for element in the_list:
        if element <= 100000:
            size += element

    print(size)

    total_used_space = max(the_list)
    target_used_space = 40000000
    print(total_used_space)
    min_file_size = total_used_space - target_used_space
    min_diff = total_used_space
    min_folder_size = 0

    for folder in the_list:
        if folder >= min_file_size:
            if folder - min_file_size < min_diff:
                min_diff = folder - min_file_size
                min_folder_size = folder

    print(min_diff)
    print(min_folder_size)


def folder_size(lines, the_list):
    size = 0
    sub_level = 0
    name = ''
    row = 0
    for line in lines:
        row += 1
        if '$' not in line and sub_level == 0:
            if 'dir' not in line:
                size += int(line.split(' ')[0])
        if ' cd ' in line:
            if '..' in line:
                if sub_level == 0:
                    the_list.append(size)
                    return size
                sub_level -= 1
            else:
                if sub_level == 0:
                    size += folder_size(lines[row:], the_list)
                sub_level += 1
    the_list.append(size)
    return size


if __name__ == "__main__":
    main()
