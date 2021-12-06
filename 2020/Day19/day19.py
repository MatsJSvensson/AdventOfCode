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
    rules = parse_input(rules)
    rexp = re.compile('^' + build_regexp(rules) + '$')
    valid = 0

    for msg in map(str.rstrip, messages):
        if rexp.match(msg):
            valid += 1

    print("valid: {}".format(valid))


def build_regexp(rules, rule=0):
    if rule == 8:
        return '(' + build_regexp(rules, 42) + ')+'

    if rule == 11:
        a = build_regexp(rules, 42)
        b = build_regexp(rules, 31)

        options = []
        for n in range(1, 40):
            options.append('{a}{{{n}}}{b}{{{n}}}'.format(a=a, b=b, n=n))

        return '(' + '|'.join(options) + ')'

    rule = rules[rule]
    if type(rule) is str:
        return rule

    options = []
    for option in rule:
        opt = ''
        for sub_rule in option:
            opt += build_regexp(rules, sub_rule)
        options.append(opt)

    return '(' + '|'.join(options) + ')'

def parse_input(fin):
    rules = {}

    for line in map(str.rstrip, fin):
        rule_id, options = line.split(': ')
        rule_id = int(rule_id)

        if '"' in options:
            rule = options[1:-1]
        else:
            rule = []
            for option in options.split('|'):
                rule.append(tuple(map(int, option.split())))

        rules[rule_id] = rule

    return rules


if __name__ == "__main__":
    main()