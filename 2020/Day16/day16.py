import argparse
import sys
import re
import os, os.path
import math

def main():
    f = open("input.txt", "r")
    input = f.read().split('\n\n')

    instructions = input[0].split('\n')

    myTicket = input[1].split('\n')[1].split(',')

    tickets = input[2].split('\n')[1:]

    validNumbers = []
    matrix = []
    order = []
    spaceToClassList = []
    for ins in instructions:
        temp = ins.split(': ')[1]
        nums = temp.split(' or ')
        nums1 = nums[0].split('-')
        nums2 = nums[1].split('-')
        for x in range(int(nums1[0]),int(nums1[1])+1):
            if x not in validNumbers:
                validNumbers.append(x)
        for x in range(int(nums2[0]),int(nums2[1])+1):
            if x not in validNumbers:
                validNumbers.append(x)
        matrix.append([])
        order.append('')
        spaceToClassList.append([])

    invalidSum = 0
    print(len(tickets))
    tempTickets = tickets.copy()
    for ticket in tempTickets:
        nums = ticket.split(',')
        invalid = False
        for y in range(len(nums)):
            num = int(nums[y])
            if num not in validNumbers:
                invalidSum += num
                invalid = True
                #print(num)
        if invalid:
            #print("remove: {}".format(ticket))
            tickets.remove(ticket)
    print(len(tickets))
    for ticket in tickets:
        nums = ticket.split(',')
        for y in range(len(nums)):
            num = int(nums[y])
            matrix[y].append(num)


    print(invalidSum)

    classToSpaceList = []

    for ins in instructions:
        classToSpace = []
        validNumbers = []
        temp = ins.split(': ')
        nums = temp[1].split(' or ')
        nums1 = nums[0].split('-')
        nums2 = nums[1].split('-')
        for x in range(int(nums1[0]), int(nums1[1]) + 1):
            if x not in validNumbers:
                validNumbers.append(x)
        for x in range(int(nums2[0]), int(nums2[1]) + 1):
            if x not in validNumbers:
                validNumbers.append(x)

        for x in range(len(matrix)):
            row = matrix[x]
            valid = True
            for y in row:
                if y not in validNumbers:
                    valid = False
                    #print("{} is invalid due to {}".format(temp[0],y))
                    break
            if valid:
                order[x] = temp[0]
                classToSpace.append(x)
                spaceToClassList[x].append(temp[0])
                #print(spaceToClassList[x])
        classToSpaceList.append(classToSpace)

    #print(order)
    #print(classToSpaceList)
    #for space in spaceToClassList:
        #print(space)

    while(True):
        counter = 0
        for x in range(len(spaceToClassList)):
            space = spaceToClassList[x]

            if len(space) == 1:
                theSpace = space[0]
                order[x] = theSpace
                for list in spaceToClassList:
                    try:
                        list.remove(theSpace)
                    except:
                        hej = 1
            if len(space) == 0:
                counter += 1
        if counter == len(spaceToClassList):
            break

    print(order)

    product = 1
    for x in range(len(order)):
        if 'departure' in order[x]:
            product *= int(myTicket[x])
    print(product)




if __name__ == "__main__":
    main()