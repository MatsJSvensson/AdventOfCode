import argparse
import sys
import re
import os, os.path

def main():
    f = open("input.txt", "r")
    input = f.read().split('\n\n')

    emptyLine = True
    valid = 0
    for instance in input:
        entries = instance.split()
        #print(entries)
        check = 0
        for entry in entries:

            entry = entry.split(':')
            type = entry[0]
            data = entry[1]

            if type in 'iyr':
                #print(type)
                if int(data) >= 2010 and int(data) <= 2020:
                    print(type)
                    check += 1
            if type in 'byr':
                #print(type)
                if int(data) >= 1920 and int(data) <= 2002:
                    print(type)
                    check += 1
            if type in 'eyr':
                #print(type)
                if int(data) >= 2020 and int(data) <= 2030:
                    print(type)
                    check += 1
            if type in 'hgt':
                #print(type)
                if data.find('in') > -1:
                    hgt = data.replace('in','')
                    if int(hgt) >= 59 and int(hgt) <= 76:
                        print(type)
                        check += 1
                elif data.find('cm') > -1:
                    #print(data)
                    hgt = data.replace('cm','')
                    #print(hgt)
                    if int(hgt) >= 150 and int(hgt) <= 193:
                        print(type)
                        check += 1
            if type in 'hcl':
                #print(type)
                if data.find('#') > -1:
                    numbers = data.replace('#', '')
                    if len(numbers) == 6:
                        cc = True
                        for char in data:
                            if "0123456789abcdef".find(char) == -1:
                                char = False
                        if cc:
                            check += 1
                            print(type)
            if type in 'ecl':
                #print(type)
                if data in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    check += 1
                    print(type)
            if type in 'pid':
                #print(type)
                if len(data) == 9:
                    for char in data:
                        cc = True
                        if "0123456789".find(char) == -1:
                            cc = False
                    if cc:
                        check += 1
                        print(type)
        print(check)
        if check >= 7:
            valid += 1


    print("Valid: {}".format(valid))




if __name__ == "__main__":
    main()