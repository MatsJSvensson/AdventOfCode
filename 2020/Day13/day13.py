import argparse
import sys
import re
import os, os.path

def main():
    f = open("input.txt", "r")
    input = f.read().split('\n')

    currentTime= int(input[0])
    entries = input[1].split(',')
    #entries = ['3','5','7']
    print(currentTime)

    minWait = 100
    theBus = -1
    maxBus = 0
    buses = []

    for bus in entries:
        if 'x' not in bus:
            bus = int(bus)
            buses.append(bus)
            latest = currentTime % bus
            wait = bus - latest
            if wait < minWait:
                minWait = wait
                theBus = bus
            print("{} {}".format(bus, wait))
            if bus > maxBus:
                maxBus = bus

    print("Solution: {} {} {}".format(theBus, minWait, theBus*minWait))

    print(maxBus)

    x = buses[0] - entries.index(str(buses[0]))
    adder = buses[0]
    for bus in buses[1:]:
        while(True):
            if bus - (x % bus) == entries.index(str(bus)) % bus:
                adder *= bus
                break
            x += adder

    print(x)

    theString = "t = {}".format(x)
    for bus in buses:
        theString = theString + ' ' + str(bus)
    print(theString)

    for y in range(x-20,x+20):
        theString = "t = {}".format(y)
        for bus in buses:
            if y % bus == 0:
                theString = theString + '  X'
            else:
                theString = theString + '  O'
        print(theString)




    # found = False
    # x = maxBus - entries.index(str(maxBus))
    # print(x)
    # while(not found):
    #     x += maxBus
    #     y = 0
    #     found = True
    #     for bus in entries:
    #         if 'x' not in bus:
    #             bus = int(bus)
    #             if not (x + y) % bus == 0:
    #                 found = False
    #                 break
    #         y += 1
    #     if found:
    #         print("The time: {}".format(x))
    #     if x % 1000 == 0:
    #         print(x)








if __name__ == "__main__":
    main()