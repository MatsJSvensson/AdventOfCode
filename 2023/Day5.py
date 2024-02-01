import argparse
import sys
import re
import os, os.path


def main():
    f = open("input5.txt", "r")
    text = f.read()
    parts = text.split('\n\n')
    seeds = parts[0].split(': ')[1].split(' ')

    maps = {}
    for part in parts[1:]:
        map = {}
        lines = part.split('\n')
        names = lines[0].split(' ')[0].split('-')
        name = names[0]
        map['target'] = names[2]
        entries = []
        for line in lines[1:]:
            entry = {}
            goal, source, length = line.split(' ')
            entry['goal'] = int(goal)
            entry['source'] = int(source)
            entry['length'] = int(length)
            inserted = False
            for x in range(len(entries)):
                if int(source) < entries[x]['source']:
                    entries.insert(x, entry)
                    inserted = True
                    break
            if not inserted:
                entries.append(entry)
        map['mappings'] = entries
        maps[name] = map

    location_to_seed = {}
    for seed in seeds:
        location = mapping(int(seed), 'seed', 'location', maps)
        location_to_seed[location] = int(seed)

    minimum = min(location_to_seed.keys())
    print(f'Location {minimum}: {location_to_seed[minimum]}')

    new_mininum = minimum*10
    for x in range(0, len(seeds), 2):
        trace = {
            'seed': [int(seeds[x]), int(seeds[x+1])]
        }
        result = mapping2(int(seeds[x]), int(seeds[x+1]), 'seed', 'location', maps, new_mininum, trace)
        if result < new_mininum:
            new_mininum = result
        print(f'{x}: {new_mininum}')

    print(f'new_minimum: {new_mininum}')


def mapping(value, source, destination, maps):
    map = maps[source]
    target = -1
    for entry in map['mappings']:
        if entry['source'] <= value < entry['source'] + entry['length']:
            target = entry['goal'] + (value - entry['source'])
    if target == -1:
        target = value

    if map['target'] == destination:
        return target
    else:
        return mapping(target, map['target'], destination, maps)


def mapping2(value, length, source, destination, maps, lowest, trace):
    map = maps[source]
    new_lowest = lowest
    if value < map['mappings'][0]['source']:
        if map['target'] == destination:
            if value < new_lowest:
                new_lowest = value
        else:
            new_trace = trace.copy()
            new_trace[map['target']] = [value, map['mappings'][0]['source'] - value]
            result = mapping2(value, map['mappings'][0]['source'] - value, map['target'], destination, maps, new_lowest, new_trace)
            if result < new_lowest:
                new_lowest = result
    for x in range(len(map['mappings'])):
        entry = map['mappings'][x]
        if value < entry['source']:
            if map['target'] == destination:
                if value < new_lowest:
                    new_lowest = value
            else:
                new_trace = trace.copy()
                new_trace[map['target']] = [value, entry['source'] - value]
                result = mapping2(value, entry['source'] - value, map['target'], destination, maps, new_lowest, new_trace)
                if result < new_lowest:
                    new_lowest = result
            length -= entry['source'] - value
            value = entry['source']
        if entry['source'] <= value < entry['source'] + entry['length']:
            if value + length <= entry['source'] + entry['length']:
                if map['target'] == destination:
                    if entry['goal'] + (value - entry['source']) < new_lowest:
                        new_lowest = entry['goal'] + (value - entry['source'])
                else:
                    new_trace = trace.copy()
                    new_trace[map['target']] = [entry['goal'] + (value - entry['source']), length]
                    result = mapping2(entry['goal'] + (value - entry['source']),
                                      length, map['target'], destination, maps, new_lowest, new_trace)
                    if result < new_lowest:
                        new_lowest = result
                break
            else:
                if map['target'] == destination:
                    if entry['goal'] + (value - entry['source']) < new_lowest:
                        new_lowest = entry['goal'] + (value - entry['source'])
                else:
                    new_trace = trace.copy()
                    new_trace[map['target']] = [entry['goal'] + (value - entry['source']), entry['length'] - (value - entry['source'])]
                    result = mapping2(entry['goal'] + (value - entry['source']),
                                      entry['length'] - (value - entry['source']),
                                      map['target'], destination, maps, new_lowest, new_trace)
                    if result < new_lowest:
                        new_lowest = result

                length -= entry['source'] + entry['length'] - value
                value = entry['source'] + entry['length']
    if map['mappings'][-1]['source'] + map['mappings'][-1]['length'] <= value:
        if map['target'] == destination:
            if value < new_lowest:
                new_lowest = value
        else:
            new_trace = trace.copy()
            new_trace[map['target']] = [value, length]
            result = mapping2(value, length, map['target'], destination, maps, new_lowest, new_trace)
            if result < new_lowest:
                new_lowest = result

    return new_lowest


if __name__ == "__main__":
    main()
