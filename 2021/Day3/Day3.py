import argparse
import sys
import re
import os, os.path
import math

def main():
    f = open("input3.txt", "r")
    input = f.read().split('\n')
    nDigits = len(input[0])
    gamma = ''
    epsilon = ''


    for n in range(nDigits):
        ones = 0
        zeroes = 0
        for line in input:
            if len(line) > 1:
                if line[n] == '0':
                    zeroes += 1
                elif line[n] == '1':
                    ones += 1
                else:
                    print('Error')
        print(f'digit {n} has {ones} ones and {zeroes} zeroes')
        if ones < zeroes:
            gamma += '0'
            epsilon +=  '1'
        else:
            gamma += '1'
            epsilon +=  '0'
    gamma_dec = 0
    epsilon_dec = 0
    for n in range(nDigits):
        gamma_dec += int(gamma[n])*math.pow(2,nDigits-n-1)
        epsilon_dec += int(epsilon[n])*math.pow(2,nDigits-n-1)
    print(f'Gamma: {gamma} - {gamma_dec}, Epsilon: {epsilon} - {epsilon_dec}, mult: {epsilon_dec*gamma_dec}')

    input_o2 = input.copy()
    input_co2 = input.copy()
    co2 = 0
    o2 = 0

    for n in range(nDigits):
        ones = 0
        zeroes = 0
        common = ''
        for line in input_o2:
            if len(line) > 1:
                if line[n] == '0':
                    zeroes += 1
                elif line[n] == '1':
                    ones += 1
                else:
                    print('Error')
        print(f'digit {n} has {ones} ones and {zeroes} zeroes')
        if ones < zeroes:
            common = '0'
        else:
            common = '1'

        temp_list = []
        for line in input_o2:
            if len(line) > 1:
                if line[n] == common:
                    temp_list.append(line)

        if len(temp_list) == 1:
            print(f'o2: {temp_list[0]}')
            o2 = temp_list[0]
            break

        input_o2 = temp_list.copy()

    for n in range(nDigits):
        ones = 0
        zeroes = 0
        common = ''
        for line in input_co2:
            if len(line) > 1:
                if line[n] == '0':
                    zeroes += 1
                elif line[n] == '1':
                    ones += 1
                else:
                    print('Error')
        print(f'digit {n} has {ones} ones and {zeroes} zeroes')
        if ones < zeroes:
            common = '1'
        else:
            common = '0'

        temp_list = []
        for line in input_co2:
            if len(line) > 1:
                if line[n] == common:
                    temp_list.append(line)

        if len(temp_list) == 1:
            print(f'co2: {temp_list[0]}')
            co2 = temp_list[0]
            break

        input_co2 = temp_list.copy()

    o2_dec = 0
    co2_dec = 0
    for n in range(nDigits):
        o2_dec += int(o2[n])*math.pow(2,nDigits-n-1)
        co2_dec += int(co2[n])*math.pow(2,nDigits-n-1)

    print(f'o2*co2: {o2_dec*co2_dec}')




if __name__ == "__main__":
    main()