import argparse
import sys
import re
import os, os.path

def main():
    f = open("input.txt", "r")
    input = f.read().split('\n')

    width = len(input[0])+2
    height = len(input)+2
    top = ''
    bottom = ''
    chairs = []

    for x in range(width):
        top += '.'
        bottom += '.'

    chairs.append(top)
    for line in input:
        line = '.' + line + '.'
        chairs.append(line)
    chairs.append(bottom)
    chairs_new = chairs.copy()

    change = True
    seated = 0
    while(change):
        change = False
        seated = 0
        for y in range(1,height-1):
            for x in range(1,width-1):


                # dirs = []
                # for r in range(8):
                #     dirs.append(False)
                # for k in range(y):
                #     if chairs[k][x] is '#':
                #         dirs[0] = True
                #         break
                #     elif chairs[k][x] is 'L':
                #         break
                # for k in range(y+1,height-1):
                #     if chairs[k][x] is '#':
                #         dirs[1] = True
                #         break
                #     elif chairs[k][x] is 'L':
                #         break
                # for k in range(x):
                #     if chairs[y][k] is '#':
                #         dirs[2] = True
                #         break
                #     elif chairs[y][k] is 'L':
                #         break
                # for k in range(x+1,width-1):
                #     if chairs[y][k] is '#':
                #         dirs[3] = True
                #         break
                #     elif chairs[y][k] is 'L':
                #         break
                #
                # lim = min(x,y)
                # for k in range(1,lim+1):
                #     if chairs[y-k][x-k] is '#':
                #         dirs[4] = True
                #         break
                #     elif chairs[y-k][x-k] is 'L':
                #         break
                # lim = min(width-x-1, height-y-1)
                # for k in range(1, lim + 1):
                #     if chairs[y + k][x + k] is '#':
                #         dirs[5] = True
                #         break
                #     if chairs[y + k][x + k] is 'L':
                #         break
                # lim = min(x, height-y-1)
                # for k in range(1, lim + 1):
                #     if chairs[y + k][x - k] is '#':
                #         dirs[6] = True
                #         break
                #     if chairs[y + k][x - k] is 'L':
                #         break
                # lim = min(width-x-1, y)
                # for k in range(1, lim + 1):
                #     if chairs[y - k][x + k] is '#':
                #         dirs[7] = True
                #         break
                #     if chairs[y - k][x + k] is 'L':
                #         break
                # tot = dirs.count(True)

                tot = 0
                tot += chairInDir(x, y,-1,-1,chairs)
                tot += chairInDir(x, y, 0, -1, chairs)
                tot += chairInDir(x, y, 1, -1, chairs)
                tot += chairInDir(x, y, 1, 0, chairs)
                tot += chairInDir(x, y, 1, 1, chairs)
                tot += chairInDir(x, y, 0, 1, chairs)
                tot += chairInDir(x, y, -1, 1, chairs)
                tot += chairInDir(x, y, -1, 0, chairs)

                if chairs[y][x] is 'L' and tot < 1:
                    chairs_new[y] = chairs_new[y][:x] + '#' + chairs_new[y][x+1:]
                    change = True
                elif chairs[y][x] is '#' and tot >= 5:
                    chairs_new[y] = chairs_new[y][:x] + 'L' + chairs_new[y][x+1:]
                    change = True
            seated += chairs_new[y].count('#')
            print(chairs_new[y])
        print("Seated: {}".format(seated))
        chairs = chairs_new.copy()

def chairInDir(x,y,xDir,yDir,chairs):
    width = len(chairs[0])
    height = len(chairs)
    chair = '.'
    while(chair is '.'):
        x += xDir
        y += yDir
        if x >= 0 and x < width and y >= 0 and y < height:
            chair = chairs[y][x]
        else:
            break
    if chair is '#':
        return 1
    else:
        return 0




if __name__ == "__main__":
    main()