import argparse
import sys
import re
import os, os.path


def main():
    f = open("input2.txt", "r")
    text = f.read()
    input = text.split('\n')
    sum = 0

    colors = {
        'green': 13,
        'red': 12,
        'blue': 14
    }

    for game in input:
        valid = True
        game, parts = game.split(': ')
        draws = parts.split('; ')
        game = int(game.split(' ')[1])
        for draw in draws:
            stones = draw.split(', ')
            for stone in stones:
                num, color = stone.split(' ')
                if int(num) > colors[color]:
                    valid = False
        if valid:
            sum += game

    print(f'sum: {sum}')

    sum = 0

    for game in input:
        colors = {
            'green': 0,
            'red': 0,
            'blue': 0
        }
        game, parts = game.split(': ')
        draws = parts.split('; ')
        game = int(game.split(' ')[1])
        for draw in draws:
            stones = draw.split(', ')
            for stone in stones:
                num, color = stone.split(' ')
                if int(num) > colors[color]:
                    colors[color] = int(num)
        sum += colors['red']*colors['green']*colors['blue']

    print(f'sum: {sum}')


if __name__ == "__main__":
    main()
