import argparse
import sys
import re
import os, os.path
import math

f = open("input16.txt", "r")
text = f.read()
lines = text.split('\n')
max_time = 30
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
    result = recursive('AA', max_time, '', 0, '', memory_map)

    print(result)


def recursive(cave, time, activated, pressure, path, memory_map):
    if time <= 0:
        return [pressure, path]
    if f'{cave} {time}' in memory_map.keys():
        if memory_map[f'{cave} {time}'] > pressure:
            return None
        else:
            memory_map[f'{cave} {time}'] = pressure
    else:
        memory_map[f'{cave} {time}'] = pressure
        
    best_result = [0, '']
    if rates[cave] != 0 and cave not in activated:
        new_activated = activated + cave + ' '
        new_pressure = pressure + (time - 1) * rates[cave]
        for new_cave in cave_map[cave]:
            result = recursive(new_cave, time-2, new_activated, new_pressure, path + f'{cave} ', memory_map)
            if result:
                if result[0] > best_result[0]:
                    best_result = result

    for new_cave in cave_map[cave]:
        last_cave = ''
        if len(path) > 0:
            last_cave = path.split(' ')[-2]
        if last_cave != new_cave:
            result = recursive(new_cave, time-1, activated, pressure, path + f'{cave} ', memory_map)
            if result:
                if result[0] > best_result[0]:
                    best_result = result
        else:
            pass
    return best_result


if __name__ == "__main__":
    main()
