import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input.txt", "r")
    input = f.read().split('\n\n')

    deck1 = input[0].split('\n')[1:]
    deck2 = input[1].split('\n')[1:]
    for x in range(len(deck1)):
        deck1[x] = int(deck1[x])
        deck2[x] = int(deck2[x])
    cd1 = deck1.copy()
    cd2 = deck2.copy()

    while(len(deck1) > 0 and len(deck2) > 0):
        a = deck1[0]
        deck1.remove(a)
        b = deck2[0]
        deck2.remove(b)

        if a > b:
            deck1.append(a)
            deck1.append(b)
        else:
            deck2.append(b)
            deck2.append(a)

    winner = []
    if len(deck1) > len(deck2):
        winner = deck1
    else:
        winner = deck2

    sum = 0
    for x in range(len(winner)):
        sum += winner[x]*(len(winner)-x)

    print(sum)

    winner = recursive(cd1,cd2,True)

    sum = 0
    for x in range(len(winner)):
        sum += winner[x] * (len(winner) - x)

    print(sum)

def recursive(deck1,deck2,origin):
    memory1 = []
    memory2 = []
    while (len(deck1) > 0 and len(deck2) > 0 and deck1 not in memory1 and deck2 not in memory2):
        cd1 = deck1.copy()
        cd2 = deck2.copy()
        memory1.append(cd1)
        memory2.append(cd2)
        a = deck1[0]
        deck1.remove(a)
        b = deck2[0]
        deck2.remove(b)

        if a > len(deck1) or b > len(deck2):
            if a > b:
                deck1.append(a)
                deck1.append(b)
            else:
                deck2.append(b)
                deck2.append(a)
        else:
            winner = recursive(deck1[:a],deck2[:b],False)
            if winner == 1:
                deck1.append(a)
                deck1.append(b)
            else:
                deck2.append(b)
                deck2.append(a)

    if min(len(deck1),len(deck2)) == 0:
        if origin:
            if len(deck1) > len(deck2):
                return deck1
            else:
                return deck2
        else:
            if len(deck1) > len(deck2):
                return 1
            else:
                return 2
    else:
        if origin:
            return deck1
        else:
            return 1





if __name__ == "__main__":
    main()