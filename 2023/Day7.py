import argparse
import sys
import re
import os, os.path


def main():
    f = open("input7.txt", "r")
    text = f.read()
    hands = text.split('\n')

    sorted = []
    card_order = '0123456789TJQKA'
    for hand in hands:
        cards, bid = hand.split(' ')
        new_hand = {'cards': cards, 'bid': int(bid)}
        counted = ''
        values = ''
        for card in cards:
            if card not in counted:
                num = cards.count(card)
                counted += card
                values += str(num)
        if '5' in values:
            new_hand['type'] = 10
        elif '4' in values:
            new_hand['type'] = 8
        elif '3' in values:
            if '2' in values:
                new_hand['type'] = 6
            else:
                new_hand['type'] = 3
        elif '2' in values:
            if values.count('2') > 1:
                new_hand['type'] = 2
            else:
                new_hand['type'] = 1
        else:
            new_hand['type'] = 0

        added = False
        for x in range(len(sorted)):
            if sorted[x]['type'] >= new_hand['type']:
                if sorted[x]['type'] == new_hand['type']:
                    for y in range(5):
                        cards2 = sorted[x]['cards']
                        card2 = card_order.find(cards2[y])
                        card1 = card_order.find(cards[y])
                        if card1 < card2:
                            #print(f'{cards2} > {card1}')
                            added = True
                            sorted.insert(x, new_hand)
                            break
                        elif card1 > card2:
                            break
                    if added:
                        break
                else:
                    added = True
                    sorted.insert(x, new_hand)
                    break
        if not added:
            sorted.append(new_hand)

    the_sum = 0
    for x in range(len(sorted)):
        bid = sorted[x]['bid']
        addition = (x+1) * bid
        the_sum += addition
        #print(f'{x+1} * {bid} = {addition}')

    print(the_sum)

    sorted = []
    card_order = 'J0123456789TQKA'
    for hand in hands:
        cards, bid = hand.split(' ')
        new_hand = {'cards': cards, 'bid': int(bid)}
        counted = ''
        values = []
        jokers = 0
        for card in cards:
            if card not in counted:
                num = cards.count(card)
                counted += card
                if card == 'J':
                    jokers = num
                else:
                    values.append(num)
        if len(values) == 0:
            values.append(0)

        if jokers > 0:
            m = max(values)
            index = values.index(m)
            values[index] += jokers

        if 5 in values:
            new_hand['type'] = 10
        elif 4 in values:
            new_hand['type'] = 8
        elif 3 in values:
            if 2 in values:
                new_hand['type'] = 6
            else:
                new_hand['type'] = 3
        elif 2 in values:
            if values.count(2) > 1:
                new_hand['type'] = 2
            else:
                new_hand['type'] = 1
        else:
            new_hand['type'] = 0

        added = False
        for x in range(len(sorted)):
            if sorted[x]['type'] >= new_hand['type']:
                if sorted[x]['type'] == new_hand['type']:
                    for y in range(5):
                        cards2 = sorted[x]['cards']
                        card2 = card_order.find(cards2[y])
                        card1 = card_order.find(cards[y])
                        if card1 < card2:
                            print(f'{cards2} > {card1}')
                            added = True
                            sorted.insert(x, new_hand)
                            break
                        elif card1 > card2:
                            break
                    if added:
                        break
                else:
                    added = True
                    sorted.insert(x, new_hand)
                    break
        if not added:
            sorted.append(new_hand)

    the_sum = 0
    for x in range(len(sorted)):
        bid = sorted[x]['bid']
        addition = (x+1) * bid
        the_sum += addition
        print(f'{x+1} * {bid} = {addition}')

    print(the_sum)


if __name__ == "__main__":
    main()
