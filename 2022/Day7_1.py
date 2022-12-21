import argparse
import sys
import re
import os, os.path


def main():
    f = open("input7.txt", "r")
    lines = f.read().split('\n')
    direct_dict = {}
    pointer_dict = {}

    size = 0
    name = ''
    for line in lines:
        if '$' not in line:
            if 'dir' in line:
                if name in pointer_dict.keys():
                    pointer_dict[name].append(line.split(' ')[1])
                else:
                    pointer_dict[name] = [line.split(' ')[1]]
            else:
                size += int(line.split(' ')[0])
        if ' cd ' in line and '..' not in line:
            if name != '':
                direct_dict[name] = size
            name = line.split(' ')[2]
            size = 0
    direct_dict[name] = size

    print(direct_dict)
    print(pointer_dict)

    total_size = {}

    for folder in direct_dict.keys():
        if folder not in pointer_dict.keys():
            total_size[folder] = direct_dict[folder]
            direct_dict.pop(folder)

    for n in range(10):
        for key in pointer_dict.keys():
            all_there = True
            for folder in pointer_dict[key]:
                if folder not in total_size.keys():
                    all_there = False

            if all_there:
                size = 0
                for folder in pointer_dict[key]:
                    size += total_size[folder]
                total_size[key] = size + direct_dict[key]
                pointer_dict.pop(key)
                direct_dict.pop(key)

        print('{} {}'.format(len(direct_dict), direct_dict))
        print('{} {}'.format(len(pointer_dict), pointer_dict))
        print('{} {}'.format(len(total_size), total_size))
        print('')



if __name__ == "__main__":
    main()
