import argparse
import sys
import re
import os, os.path
import math

f = open("input16.txt", "r")
text = f.read()
lines = text.split('\n')
max_time = 26
cave_map = {}
rates = {}
for line in lines:
    here, there = line.split(';')
    rate = int(here.split('flow rate=')[1])
    cave = here.split(' ')[1]
    rates[cave] = rate
    there = there.replace('valve ', 'valves ')
    cave_map[cave] = there.split('valves ')[1].split(', ')


def main():
    memory_map = {}
    result = recursive('AA', 'AA', max_time, '', 0, '', '', memory_map)

    print(result)


def recursive(cave1, cave2, time, activated, pressure, path1, path2, memory_map):
    if time <= 0:
        return [pressure, path1, path2]
    if f'{cave1} {cave2} {time}' in memory_map.keys():
        if memory_map[f'{cave1} {cave2} {time}'] >= pressure:
            return None
        else:
            memory_map[f'{cave1} {cave2} {time}'] = pressure
            memory_map[f'{cave2} {cave1} {time}'] = pressure
    else:
        memory_map[f'{cave1} {cave2} {time}'] = pressure
        memory_map[f'{cave2} {cave1} {time}'] = pressure

    best_result = [0, '', '']
    if rates[cave1] != 0 and cave1 not in activated:
        new_activated = activated + cave1 + ' '
        new_pressure = pressure + (time - 1) * rates[cave1]
        if rates[cave2] != 0 and cave2 not in activated:
            new_activated = activated + cave2 + ' '
            new_pressure = pressure + (time - 1) * rates[cave2]
            result = recursive(cave1, cave2, time - 1, new_activated, new_pressure,
                               path1 + f'{cave1} ', path2 + f'{cave2} ', memory_map)
            if result:
                if result[0] > best_result[0]:
                    best_result = result
        else:
            for new_cave in cave_map[cave2]:
                result = recursive(cave1, new_cave, time-1, new_activated, new_pressure,
                                   path1 + f'{cave1} ', path2 + f'{cave2} ', memory_map)
                if result:
                    if result[0] > best_result[0]:
                        best_result = result
    if rates[cave2] != 0 and cave2 not in activated:
        new_activated = activated + cave2 + ' '
        new_pressure = pressure + (time - 1) * rates[cave2]
        for new_cave in cave_map[cave1]:
            result = recursive(new_cave, cave2, time-1, new_activated, new_pressure,
                               path1 + f'{cave1} ', path2 + f'{cave2} ', memory_map)
            if result:
                if result[0] > best_result[0]:
                    best_result = result

    for new_cave1 in cave_map[cave1]:
        last_cave1 = ''
        if len(path1) > 0:
            last_cave1 = path1.split(' ')[-2]
        if last_cave1 != new_cave1:
            for new_cave2 in cave_map[cave2]:
                last_cave2 = ''
                if len(path2) > 0:
                    last_cave2 = path2.split(' ')[-2]
                if last_cave2 != new_cave2:
                    result = recursive(new_cave1, new_cave2, time-1, activated, pressure,
                                       path1 + f'{cave1} ', path2 + f'{cave2} ', memory_map)
                    if result:
                        if result[0] > best_result[0]:
                            best_result = result

    return best_result


if __name__ == "__main__":
    main()
