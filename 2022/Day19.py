import argparse
import sys
import re
import os, os.path
import math


def set_point(a_map, x, y, z, char):
    a_map[z][y] = a_map[z][y][:x] + char + a_map[z][y][x+1:]


f = open("input19.txt", "r")
text = f.read()
lines = text.split('\n')
blueprints = {}
for line in lines:
    blueprint_id = int(line.split(':')[0].split(' ')[1])
    parts = line.split('robot costs ')
    ore = parts[1].split('.')[0]
    clay = parts[2].split('.')[0]
    obsidian = parts[3].split('.')[0]
    geode = parts[4]. split('.')[0]
    ore_cost = [int(ore.split(' ')[0]), 0, 0, 0]
    clay_cost = [int(clay.split(' ')[0]), 0, 0, 0]
    obsidian_parts = obsidian.split(' and ')
    obsidian_cost = [int(obsidian_parts[0].split(' ')[0]), int(obsidian_parts[1].split(' ')[0]), 0, 0]
    geode_parts = geode.split(' and ')
    geode_cost = [int(geode_parts[0].split(' ')[0]), 0, int(geode_parts[1].split(' ')[0]), 0]
    blueprints[blueprint_id] = [ore_cost, clay_cost, obsidian_cost, geode_cost]


def main():
    robots = [1, 0, 0, 0]
    resources = [0, 0, 0, 0]
    test_counter = [0]
    print(recursive(0, robots, resources, 0, 1, test_counter))
    print(test_counter)


def recursive(time, robots, resources, next_target, blueprint, test_counter):
    test_counter[0] += 1
    for n in range(time, 24):
        afford = True
        for x in range(4):
            if resources[x] < blueprints[blueprint][next_target][x]:
                afford = False
            resources[x] += robots[x]
        if afford:
            robots[next_target] += 1
            for x in range(4):
                resources[x] -= blueprints[blueprint][next_target][x]
            new_robots = robots.copy()
            new_resources = resources.copy()
            results = []
            results.append(recursive(n+1, new_robots, new_resources, 0, blueprint, test_counter))

            new_robots = robots.copy()
            new_resources = resources.copy()
            results.append(recursive(n + 1, new_robots, new_resources, 1, blueprint, test_counter))
            if robots[1] > 0:
                new_robots = robots.copy()
                new_resources = resources.copy()
                results.append(recursive(n + 1, new_robots, new_resources, 2, blueprint, test_counter))
            if robots[2] > 0:
                new_robots = robots.copy()
                new_resources = resources.copy()
                results.append(recursive(n + 1, new_robots, new_resources, 3, blueprint, test_counter))
            return max(results)
    print(resources)
    return resources[3]


if __name__ == "__main__":
    main()
