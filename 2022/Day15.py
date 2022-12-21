import argparse
import sys
import re
import os, os.path
import math

f = open("input15.txt", "r")
text = f.read()
lines = text.split('\n')


def main():
    specific_row = 2000000
    rows = []
    for specific_row in range(0, 4000000):
        blocked_x = []
        for line in lines:
            sensor, beacon = line.split(':')
            sensor_x, sensor_y = sensor.split(',')
            beacon_x, beacon_y = beacon.split(',')
            beacon_x = int(beacon_x.split('x=')[1])
            beacon_y = int(beacon_y.split('y=')[1])
            sensor_x = int(sensor_x.split('x=')[1])
            sensor_y = int(sensor_y.split('y=')[1])
            distance1 = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            distance2 = abs(sensor_y - specific_row)
            if distance2 < distance1:
                x_diff = distance1 - distance2
                x_min = sensor_x - x_diff
                x_max = sensor_x + x_diff
                included = False
                for n in range(len(blocked_x)):
                    if x_min < blocked_x[n][0]:
                        if x_max < blocked_x[n][0]:
                            blocked_x.insert(n, [x_min, x_max])
                        elif x_max <= blocked_x[n][1]:
                            blocked_x[n][0] = x_min
                        else:
                            blocked_x[n] = [x_min, x_max]
                        included = True
                        break
                    elif x_min <= blocked_x[n][1]:
                        if x_max < blocked_x[n][1]:
                            pass
                        else:
                            blocked_x[n][1] = x_max
                        included = True
                if not included:
                    blocked_x.append([x_min, x_max])

        popped = True
        while popped:
            popped = False
            for n in range(1, len(blocked_x)):
                if blocked_x[n-1][1] + 1 >= blocked_x[n][0]:
                    if blocked_x[n-1][1] < blocked_x[n][1]:
                        blocked_x[n-1][1] = blocked_x[n][1]
                    blocked_x.pop(n)
                    popped = True
                    break
        rows.append(blocked_x)

    for n in range(len(rows)):
        if len(rows[n]) > 1:
            print(f'{n}: {rows[n]}')
            if rows[n][1][0] - rows[n][0][1] == 2:
                x = rows[n][0][1] + 1
                result = 4000000 * x + n
                print(f'frequency: {result}')


if __name__ == "__main__":
    main()
