import argparse
import sys
import re
import os, os.path
import math

eight = []
eleven = []
fortytwo = []
thirtyone = []

def main():
    f = open("input.txt", "r")
    input = f.read().split('\n\n')

    rules = input[0].split('\n')
    messages = input[1].split('\n')

    ordered = ['']*len(rules)
    for rule in rules:
        parts = rule.split(': ')
        ordered[int(parts[0])] = parts[1]

    valid = buildRules(ordered,0,messages)

    global eight
    global eleven
    global thirtyone
    global fortytwo

    print(eight)
    print(eleven)

    count = 0
    for message in messages:
        if message in valid:
            count += 1

    print(count)

def buildRules(rules, x, messages):
    alts = rules[x].split(' | ')
    result = []
    for alt in alts:
        parts = alt.split(' ')
        reLists = []

        for part in parts:
            if '"' in part:
                part = part.replace('"','')
                return [part]
            else:
                reLists.append(buildRules(rules,int(part),messages))
        if len(reLists) > 1:
            for i in range(len(reLists[0])):
                for j in range(len(reLists[1])):
                    result.append(reLists[0][i] + reLists[1][j])
        else:
            result.extend(reLists[0])

    if x == 8:
        global eight
        eight = result.copy()
        recursiveEight(eight,messages)

    if x == 11:
        global eleven
        eleven = result.copy()

    if x == 31:
        global thirtyone
        thirtyone = result.copy()

    if x == 42:
        global fortytwo
        fortytwo = result.copy()

    return result

def recursiveEight(newEight, messages):
    global fortytwo
    global eight

    temp = []
    for message in messages:
        for e in newEight:
            for f in fortytwo:
                newMess = f + e
                if newMess in message:
                    if newMess not in temp:
                        temp.append(f + e)

    if len(temp) > 0:
        eight.extend(temp)
        recursiveEight(temp, messages)


if __name__ == "__main__":
    main()