import argparse
import sys
import re
import os, os.path
import math

globalPictures = []

def main():
    f = open("input.txt", "r")
    input = f.read().split('\n\n')

    tiles = []
    gridSize = 12

    for tile in input:
        theTile = dict()
        lines = tile.split('\n')
        tileSize = len(lines[1])
        theTile['ID'] = int(lines[0].replace('Tile ','').replace(':',''))
        borders = ['','','','']
        borders[0] = lines[1]
        borders[3] = lines[10]
        for x in range(tileSize):
            borders[1] += lines[x+1][0]
            borders[2] += lines[x+1][9]
        center = []
        for i in range(2,tileSize):
            center.append(lines[i][1:tileSize-1])
        theTile['center'] = center
        theTile['borders'] = borders
        tiles.append(theTile)

    theGrid = []
    for i in range(gridSize):
        aList = []
        for j in range(gridSize):
            aList.append({})
        theGrid.append(aList)


    for tile in tiles:
        theGrid[0][0] = tile
        tsc = tiles.copy()
        tsc.remove(tile)
        for i in range(4):
            recursive(tsc,0,0,theGrid)
            tile = rotateTile(tile)
        print(tile['ID'])

    global globalPictures
    monsters = 0
    for picture in globalPictures:
        for i in range(8):
            monsters = checkMonsters(picture)
            picture = rotatePic(picture)
            if i == 3:
                picture = flipPic(picture)
        print('')

    sum = 0
    for row in globalPictures[0]:
        sum += row.count('#')
    print('Number of #: {} - 15 * {} = {}'.format(sum, monsters, sum - monsters*15))


def recursive(tiles, x, y, grid):
    theTile = grid[x][y]
    gridSize = len(grid[0])
    if x < gridSize-1:
        for tile in tiles:
            match = False
            tc = tile.copy()
            tc['borders'] = tile['borders'].copy()
            tc['center'] = tile['center'].copy()
            for border in tile['borders']:
                if border in theTile['borders'][2] or border[::-1] in theTile['borders'][2]:
                    match = True
            if match:
                match = False
                for k in range(7):
                    if tc['borders'][1] in theTile['borders'][2]:
                        if y > 0:
                            if tc['borders'][0] in grid[x+1][y-1]['borders'][3]:
                                match = True
                                break
                        else:
                            match = True
                            break
                    tc = rotateTile(tc)
                    if k == 3:
                        tc = flipTile(tc)
                if match:
                    gc = grid.copy()
                    gc[x+1][y] = tc
                    tsc = tiles.copy()
                    tsc.remove(tile)
                    recursive(tsc,x+1,y,gc)

    elif y < gridSize-1:
        x = 0
        theTile = grid[x][y]
        for tile in tiles:
            match = False
            tc = tile.copy()
            tc['borders'] = tile['borders'].copy()
            tc['center'] = tile['center'].copy()
            for border in tile['borders']:
                if border in theTile['borders'][3] or border[::-1] in theTile['borders'][3]:
                    match = True
            if match:
                match = False
                for k in range(8):
                    if tc['borders'][0] in theTile['borders'][3]:
                        if x > 0:
                            if tc['borders'][1] in grid[x-1][y+1]['borders'][2]:
                                match = True
                                break
                        else:
                            match = True
                            break
                    tc = rotateTile(tc)
                    if k == 3:
                        tc = flipTile(tc)
                if match:
                    gc = grid.copy()
                    gc[x][y+1] = tc
                    tsc = tiles.copy()
                    tsc.remove(tile)
                    recursive(tsc,x,y+1,gc)

    else:
        c1 = grid[0][0]['ID']
        c2 = grid[0][gridSize-1]['ID']
        c3 = grid[gridSize-1][0]['ID']
        c4 = grid[gridSize-1][gridSize-1]['ID']
        product = c1*c2*c3*c4
        print("{} {} {} {} {}".format(c1,c2,c3,c4,product))

        global globalPictures
        picture = []
        for y in range(gridSize):
            for i in range(8):
                line = ''
                for x in range(gridSize):
                    line += grid[x][y]['center'][i]
                print(line)
                picture.append(line)
        print('')
        globalPictures.append(picture)

def rotateTile(tile):
    printing = False
    if printing:
        print(tile['borders'][0])
        for i in range(8):
            print("{}{}{}".format(tile['borders'][1][i+1],tile['center'][i],tile['borders'][2][i+1]))
        print(tile['borders'][3])
        print('')

    temp = tile['borders'][0]
    tile['borders'][0] = tile['borders'][2]
    tile['borders'][2] = tile['borders'][3][::-1]
    tile['borders'][3] = tile['borders'][1]
    tile['borders'][1] = temp[::-1]

    centerSize = len(tile['center'][0])
    tempCenter = []
    for i in range(centerSize):
        row = ''
        for j in range(centerSize):
            row += tile['center'][j][centerSize-i-1]
        tempCenter.append(row)
    tile['center'] = tempCenter
    return tile

def rotatePic(pic):
    picSize = len(pic[0])
    tempPic = []
    for i in range(picSize):
        row = ''
        for j in range(picSize):
            row += pic[j][picSize-i-1]
        tempPic.append(row)
    return tempPic

def flipTile(tile):
    printing = False
    if printing:
        print(tile['borders'][0])
        for i in range(8):
            print("{}{}{}".format(tile['borders'][1][i + 1], tile['center'][i], tile['borders'][2][i + 1]))
        print(tile['borders'][3])
        print('')

    temp = tile['borders'][1]
    tile['borders'][1] = tile['borders'][2]
    tile['borders'][2] = temp
    tile['borders'][0] = tile['borders'][0][::-1]
    tile['borders'][3] = tile['borders'][3][::-1]

    tempCenter = []
    for i in range(len(tile['center'][0])):
        tempCenter.append(tile['center'][i][::-1])
    tile['center'] = tempCenter

    if printing:
        print(tile['borders'][0])
        for i in range(8):
            print("{}{}{}".format(tile['borders'][1][i + 1], tile['center'][i], tile['borders'][2][i + 1]))
        print(tile['borders'][3])
        print('')

    return tile

def flipPic(pic):
    picSize = len(pic[0])
    tempPic = []
    for i in range(picSize):
        tempPic.append(pic[i][::-1])

    return tempPic

def checkMonsters(picture):
    monster1 = '                  # '
    monster2 = '#    ##    ##    ###'
    monster3 = ' #  #  #  #  #  #   '

    monsters = 0
    picSize = len(picture)

    for x in range(picSize-20):
        for y in range(picSize-3):
            pc = picture.copy()
            exist = True
            for i in range(20):
                if monster1[i] in '#':
                    if picture[y][x+i] not in '#':
                        exist = False
                        break
                    else:
                        pc[y] = pc[y][:x+i] + 'O' + pc[y][x+i+1:]
                if monster2[i] in '#':
                    if picture[y+1][x+i] not in '#':
                        exist = False
                        break
                    else:
                        pc[y+1] = pc[y+1][:x+i] + 'O' + pc[y+1][x+i+1:]
                if monster3[i] in '#':
                    if picture[y+2][x+i] not in '#':
                        exist = False
                        break
                    else:
                        pc[y+2] = pc[y+2][:x + i] + 'O' + pc[y+2][x + i + 1:]
            if i > 19:
                for line in pc:
                    print(line)
                print('')
            if exist:
                monsters += 1
    return monsters
if __name__ == "__main__":
    main()