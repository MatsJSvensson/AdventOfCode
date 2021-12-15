import argparse
import sys
import re
import os, os.path
import math

def main():
    f = open("input8.txt", "r")
    the_input = f.readlines()
    first_sum = 0
    second_sum = 0

    for line in the_input:
        place_b = ''
        place_d = ''

        digit_combos = ['','','','','','','','','','']

        if len(line) > 1:
            digit_string, output_string = line.split('|')
            digits = digit_string.split(' ')
            output = output_string.strip().split(' ')

            for digit in digits:
                l = len(digit)
                if l == 2:
                    digit_combos[1] = digit
                elif l == 3:
                    digit_combos[7] = digit
                elif l == 4:
                    digit_combos[4] = digit
                elif l == 7:
                    digit_combos[8] = digit

            place_c = digit_combos[1]
            place_f = digit_combos[1]
            for letter in digit_combos[7]:
                if letter not in digit_combos[1]:
                    place_a = letter
            for letter in digit_combos[4]:
                if letter not in digit_combos[1]:
                    place_b += letter
                    place_d += letter

            for digit in digits:
                l = len(digit)
                if l == 5:
                    if digit_combos[1][0] in digit and digit_combos[1][1] in digit:
                        digit_combos[3] = digit
                    elif place_b[0] in digit and place_d[1] in digit:
                        digit_combos[5] = digit
                    else:
                        digit_combos[2] = digit
                elif l == 6:
                    if digit_combos[1][0] not in digit or digit_combos[1][1] not in digit:
                        digit_combos[6] = digit
                    elif place_b[0] not in digit or place_d[1] not in digit:
                        digit_combos[0] = digit
                    else:
                        digit_combos[9] = digit

            sequence = ''
            for digit in output:
                l = len(digit)
                if l in [2,3,4,7]:
                    first_sum += 1
                for n in range(10):
                    if l == len(digit_combos[n]):
                        correct = True
                        for letter in digit:
                            if letter not in digit_combos[n]:
                                correct = False
                                break
                        if correct:
                            sequence += str(n)
                            break
            print(sequence)
            second_sum += int(sequence)



    print(f'sums = {first_sum}, {second_sum}')


if __name__ == "__main__":
    main()