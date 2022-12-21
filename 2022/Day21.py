import argparse
import sys
import re
import os, os.path
import math

f = open("input21.txt", "r")
text = f.read()
lines = text.split('\n')
monkeys = {}
for line in lines:
    name, command = line.split(': ')
    monkeys[name] = command


def main():
    result = recursive('root')
    print(result)
    words = monkeys['root'].split(' ')
    a = words[0]
    b = words[2]
    print(recursive(a))
    print(recursive(b))
    monkeys['humn'] = '0'
    print(recursive(a))
    print(recursive(b))
    target = recursive(b)
    recursive2(a, target)


def recursive(monkey):
    words = monkeys[monkey].split(' ')
    if len(words) > 1:
        a = recursive(words[0])
        b = recursive(words[2])
        result = None
        if words[1] == '+':
            result = a + b
        elif words[1] == '-':
            result = a - b
        elif words[1] == '*':
            result = a * b
        elif words[1] == '/':
            result = a / b
        else:
            print('bad input')
        return result
    else:
        return int(words[0])


def check_for_human(monkey):
    words = monkeys[monkey].split(' ')
    if len(words) > 1:
        a = words[0]
        b = words[2]
    else:
        return False
    if a == 'humn' or b == 'humn':
        return True

    if check_for_human(a) or check_for_human(b):
        return True
    else:
        return False


def recursive2(monkey, target):
    if monkey == 'humn':
        print(f'humn = {target}')
    words = monkeys[monkey].split(' ')
    if len(words) > 1:
        if check_for_human(words[0]):
            a = None
        else:
            a = recursive(words[0])
        if check_for_human(words[2]):
            b = None
        else:
            b = recursive(words[2])

        if a and b:
            result = None
            if words[1] == '+':
                result = a + b
            elif words[1] == '-':
                result = a - b
            elif words[1] == '*':
                result = a * b
            elif words[1] == '/':
                result = a / b
            else:
                print('bad input')
            return result
        else:
            if words[1] == '+':
                if a:
                    new_target = target - a
                    recursive2(words[2], new_target)
                else:
                    new_target = target - b
                    recursive2(words[0], new_target)
            elif words[1] == '-':
                if a:
                    new_target = a - target
                    recursive2(words[2], new_target)
                else:
                    new_target = target + b
                    recursive2(words[0], new_target)
            elif words[1] == '*':
                if a:
                    new_target = target / a
                    recursive2(words[2], new_target)
                else:
                    new_target = target / b
                    recursive2(words[0], new_target)
            elif words[1] == '/':
                if a:
                    new_target = a / target
                    recursive2(words[2], new_target)
                else:
                    new_target = target * b
                    recursive2(words[0], new_target)
            else:
                print('bad input')


if __name__ == "__main__":
    main()
