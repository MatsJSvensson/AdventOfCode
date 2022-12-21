import argparse
import sys
import re
import os, os.path
import math

f = open("input20.txt", "r")
text = f.read()
original_lines = text.split('\n')


def main():
    lines = original_lines.copy()
    length = len(lines)
    for line in original_lines:
        index = lines.index(line)
        new_index = (index + int(line)) % (length - 1)
        lines.remove(line)
        lines.insert(new_index, line)

    index0 = lines.index('0')
    a = int(lines[(index0+1000) % length])
    b = int(lines[(index0+2000) % length])
    c = int(lines[(index0+3000) % length])
    print(f'{a} + {b} + {c} = {a+b+c}')


def get_checksum(numbers):
    summed = 0
    indices = [1000, 2000, 3000]

    # Find the index of the zero
    for index_zero, x in enumerate(numbers):
        if x[1] == 0:
            break

    # Get the checksum
    for i in indices:
        summed += numbers[(index_zero + i) % len(numbers)][1]
    return summed


def shuffle(numbers, original_numbers):
    for i, line in enumerate(original_numbers):
        number = int(line)
        tofind = (i, number)

        # Find where the number is
        index = numbers.index(tofind)

        # Concatenate the left and right list and find the new position
        left_list = numbers[:index]
        right_list = numbers[index + 1:]
        temp = left_list + right_list

        # Insert the number at the new position
        # TODO: I seem to have some issues with either adding the number to the end or the beginning
        # However, for the checksum that is not relevant, so I just add it to the end
        newpos = (index + number) % len(temp)
        if newpos == 0:
            temp.append(tofind)
        else:
            temp.insert(newpos, tofind)

        # Update the numbers
        numbers = temp

    return numbers


def get_init(decryption_key=1):
    lines = open('input20.txt').readlines()
    lines = [line.strip() for line in lines]

    # As we need to shuffle the numbers in the order they originally appear,
    # we need to keep track of the original position
    numbers = [(i, int(x) * decryption_key) for i, x in enumerate(lines)]
    original_numbers = [x[1] for x in numbers]
    return numbers, original_numbers


numbers, original = get_init(decryption_key=1)
numbers = shuffle(numbers, original)
print('part 1', get_checksum(numbers))

# For part 2 we simply shuffle 10 times, but init with a different decryption key
numbers, original = get_init(decryption_key=811589153)
for i in range(10):
    print(i)
    shuffled = shuffle(numbers, original)
    numbers = shuffled
print('part 2', get_checksum(numbers))


if __name__ == "__main__":
    main()
