import argparse
import sys
import re
import os, os.path
import math

def main():
    f = open("input.txt", "r")
    input = f.read().split('\n')

    cycles = 6
    axis = len(input[0])
    matrix = newMatrix(axis,cycles)

    for x in range(axis):
        for y in range(axis):
            matrix[x+cycles+1][y+cycles+1][cycles+1][cycles+1] = input[x][y]

    #printMatrix(matrix)

    for t in range(cycles):
        matrixCopy = newMatrix(axis,cycles)
        size = len(matrix)
        for z in range(1, len(matrix[0][0]) - 1):
            for w in range(1, len(matrix[0][0]) - 1):
                for x in range(1, size - 1):
                    for y in range(1, size - 1):
                        sum = 0
                        for k in range(3):
                            for l in range(3):
                                for m in range(3):
                                    for n in range(3):
                                        if matrix[x+k-1][y+l-1][z+m-1][w+n-1] in '#':
                                            sum += 1
                        if matrix[x][y][z][w] in '#':
                            if sum == 3 or sum == 4:
                                matrixCopy[x][y][z][w] = '#'
                            else:
                                matrixCopy[x][y][z][w] = '.'
                        else:
                            if sum == 3:
                                matrixCopy[x][y][z][w] = '#'
                            else:
                                matrixCopy[x][y][z][w] = '.'
        matrix = matrixCopy
        print("Generation {}".format(t))
        #printMatrix(matrix)

    print(endSum(matrix))


def printMatrix(matrix):
    size = len(matrix)
    for z in range(1,len(matrix[0][0])-1):
        for x in range(1,size-1):
            line = ''
            for y in range(1,size-1):
                line += matrix[x][y][z]
            print(line)
        print('\n')

def newMatrix(size,cycles):
    matrix = []
    for k in range(size + (cycles+1)*2):
        x = []
        matrix.append(x)
        for l in range(size + (cycles+1)*2):
            y = []
            x.append(y)
            for m in range(1 + (cycles+1)*2):
                z = []
                y.append(z)
                for n in range(1 + (cycles+1)*2):
                    z.append('-')
    return matrix

def endSum(matrix):
    sum = 0
    for x in matrix:
        for y in x:
            for z in y:
                for w in z:
                    if w in '#':
                        sum += 1
    return sum





if __name__ == "__main__":
    main()