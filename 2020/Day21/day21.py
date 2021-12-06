import argparse
import sys
import re
import os, os.path
import math


def main():
    f = open("input.txt", "r")
    input = f.read().split('\n')

    ingredientsList = []
    allergensList = []
    allergensDict = {}


    for dish in input:
        parts = dish.split(' (contains ')
        ingredients = parts[0].split(' ')
        allergens = parts[1].replace(')','')
        allergens = allergens.split(', ')

        for ingredient in ingredients:
            if ingredient not in ingredientsList:
                ingredientsList.append(ingredient)
        for allergen in allergens:
            if allergen not in allergensList:
                allergensList.append(allergen)
        for allergen in allergens:
            if allergen not in allergensDict.keys():
                allergensDict[allergen] = ingredients.copy()
            else:
                tempList = allergensDict[allergen].copy()
                for ingredient in allergensDict[allergen]:
                    if ingredient not in ingredients:
                        tempList.remove(ingredient)
                allergensDict[allergen] = tempList

    change = True
    while(change):
        change = False
        for allergen in allergensDict.keys():
            if len(allergensDict[allergen]) == 1:
                ingredient = allergensDict[allergen][0]
                for allergen2 in allergensDict.keys():
                    if allergen != allergen2 and ingredient in allergensDict[allergen2]:
                        allergensDict[allergen2].remove(ingredient)
                        change = True

    for allergen in allergensDict.keys():
        for ingredient in allergensDict[allergen]:
            print(len(ingredientsList))
            if ingredient in ingredientsList:
                ingredientsList.remove(ingredient)
            print(len(ingredientsList))

    sum = 0
    for ingredient in ingredientsList:
        partSum = 0
        for row in input:
            partSum += (' ' + row).count(' ' + ingredient + ' ')
        sum += partSum
        #print('{} {}'.format(ingredient, partSum))

    sortList = allergensList.copy()
    sortList.sort()
    dangerous = ''
    for allergen in sortList:
        dangerous += allergensDict[allergen][0] + ','

    print(allergensDict)
    print(allergensList)
    print(sum)
    print(dangerous)

if __name__ == "__main__":
    main()