import argparse
import sys
import re
import os, os.path


def main():
    f = open("input2.txt", "r")
    input = f.read().split('\n')
    total_score = 0
    for line in input:
        hands = line.split(' ')
        score = 0
        if hands[1] == 'X':
            score += 1
            if hands[0] == 'A':
                score += 3
            elif hands[0] == 'C':
                score += 6
        elif hands[1] == 'Y':
            score += 2
            if hands[0] == 'B':
                score += 3
            elif hands[0] == 'A':
                score += 6
        if hands[1] == 'Z':
            score += 3
            if hands[0] == 'C':
                score += 3
            elif hands[0] == 'B':
                score += 6
        total_score += score

    total_score2 = 0
    for line in input:
        hands = line.split(' ')
        score = 0
        if hands[1] == 'X':
            if hands[0] == 'A':
                score += 3
            elif hands[0] == 'B':
                score += 1
            elif hands[0] == 'C':
                score += 2
        elif hands[1] == 'Y':
            score += 3
            if hands[0] == 'A':
                score += 1
            elif hands[0] == 'B':
                score += 2
            elif hands[0] == 'C':
                score += 3
        elif hands[1] == 'Z':
            score += 6
            if hands[0] == 'A':
                score += 2
            elif hands[0] == 'B':
                score += 3
            elif hands[0] == 'C':
                score += 1
        total_score2 += score

        print(f'score 2: {score}')

    print(f'total score: {total_score}')
    print(f'total score 2: {total_score2}')
    # print(f'top3: {top3}')


if __name__ == "__main__":
    main()
