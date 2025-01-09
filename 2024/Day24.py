import argparse
import sys
import re
import os, os.path
import math
import aoc_utils as utils
import time

f = open("input24.txt", "r")
text = f.read()
parts = text.split('\n\n')


def main():
    values_org = {}
    for line in parts[0].split('\n'):
        name, val = line.split(': ')
        values_org[name] = int(val)

    operations_org = {}
    for line in parts[1].split('\n'):
        ops, out = line.split(' -> ')
        n1, operand, n2 = ops.split(' ')
        operations_org[out] = {'operand': operand, 'in1': n1, 'in2': n2}

    operations = operations_org.copy()
    values = values_org.copy()

    values = execute(operations, values)

    out_values = {}
    out_list = []
    x_list = []
    y_list = []
    for name in values.keys():
        if name.startswith('z'):
            out_values[name] = values[name]
            out_list.append(name)
        if name.startswith('x'):
            x_list.append(name)
        if name.startswith('y'):
            y_list.append(name)
    out_list.sort()
    x_list.sort()
    y_list.sort()

    the_sum = binary(out_list, out_values)
    print(the_sum)

    x = binary(x_list, values)
    y = binary(y_list, values)
    potentials1 = []
    potentials2 = []

    for val in operations_org.keys():
        op = operations_org[val]
        if val.startswith('z') and val != 'z45':
            if op['operand'] != 'XOR':
                potentials1.append(val)
        else:
            if not (op['in1'].startswith('x') or op['in1'].startswith('y')):
                if op['operand'] == 'XOR':
                    potentials2.append(val)

    print(potentials1)
    print(potentials2)
    pairs = {}
    for p_in in potentials2:
        res = recurse_out(p_in, potentials1, operations_org)
        res.sort()
        first = int(res[0].replace('z', ''))
        target = f'z{first - 1}'
        if target in potentials1:
            pairs[p_in] = target
    print(pairs)

    for p in pairs.keys():
        q = pairs[p]
        temp = operations_org[p]
        operations_org[p] = operations_org[q]
        operations_org[q] = temp

    operations = operations_org.copy()
    values = values_org.copy()
    values = execute(operations, values)
    new_sum = binary(out_list, values)
    target = x + y
    string_bin = f'{bin(new_sum ^ target)}'.replace('0b', '')
    print(string_bin)
    index = len(string_bin) - string_bin.find('0')
    print(index)
    tx = f'x{index}'
    ty = f'y{index}'

    potentials3 = []
    for val in operations_org.keys():
        op = operations_org[val]
        if op['in1'] == tx and op['in2'] == ty or op['in2'] == tx and op['in1'] == ty:
            potentials3.append(val)
    print(potentials3)
    pairs[potentials3[0]] = potentials3[1]
    temp = operations_org[potentials3[0]]
    operations_org[potentials3[0]] = operations_org[potentials3[1]]
    operations_org[potentials3[1]] = temp

    operations = operations_org.copy()
    values = values_org.copy()
    values = execute(operations, values)
    new_sum = binary(out_list, values)
    print(f'New sum: {new_sum}, Target: {target}')

    big_list = potentials1 + potentials2 + potentials3
    big_list.sort()
    print(','.join(big_list))


def recurse_out(p_in, potentials, operations):
    outs = []
    for p in operations.keys():
        if p_in == operations[p]['in1'] or p_in == operations[p]['in2']:
            if 'z' in p:
                outs.append(p)
            else:
                outs.extend(recurse_out(p, potentials, operations))
    return outs


def binary(a_list, a_dict):
    the_sum = 0
    for i in range(len(a_list)):
        the_sum += a_dict[a_list[i]] * pow(2, i)
    return the_sum


def execute(operations, values):
    while len(operations) > 0:
        temp = operations.keys()
        names = list(temp).copy()
        for name in names:
            op = operations[name]
            in1 = op['in1']
            in2 = op['in2']
            if in1 in values and in2 in values:
                result = perform_operation(values[in1], values[in2], op['operand'])
                if result is not None:
                    values[name] = result
                    operations.pop(name)
    return values


def perform_operation(arg1, arg2, operand):
    output = None
    if operand == 'AND':
        output = 0
        if arg1 == 1 and arg2 == 1:
            output = 1
    if operand == 'OR':
        output = 0
        if arg1 == 1 or arg2 == 1:
            output = 1
    if operand == 'XOR':
        output = 0
        if arg1 != arg2:
            output = 1

    return output


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f'Total runtime: {time.time() - start_time}s')
