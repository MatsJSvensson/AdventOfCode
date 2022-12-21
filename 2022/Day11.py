import argparse
import sys
import re
import os, os.path
import math


class Monkey:
    def __init__(self, text):
        lines = text.split('\n')
        self.monkey_id = int(lines[0].replace(':', '').split(' ')[1])
        self.items = lines[1].split(': ')[1].split(', ')
        if self.items[0] == '':
            self.items.clear()
        for n in range(len(self.items)):
            self.items[n] = int(self.items[n])
        self.operation = lines[2].split('= ')[1]
        self.test_value = int(lines[3].split('by ')[1])
        self.true_receiver = int(lines[4].split('monkey ')[1])
        self.false_receiver = int(lines[5].split('monkey ')[1])
        self.observations = 0

    def run_operation(self):
        self.observations += len(self.items)

        parts = self.operation.split(' ')
        second_part = parts[2]
        for n in range(len(self.items)):
            item = self.items[n]
            if second_part == 'old':
                value = item
            else:
                value = int(second_part)
            result = 0
            if parts[1] == '+':
                result = item + value
            elif parts[1] == '*':
                result = item * value
            else:
                print('Error!')
            self.items[n] = result

    def test(self, monkeys):
        for item in self.items:
            if item % self.test_value == 0:
                monkeys[self.true_receiver].items.append(item)
            else:
                monkeys[self.false_receiver].items.append(item)
        self.items.clear()

    def relief(self):
        for n in range(len(self.items)):
            self.items[n] = self.items[n] // 3


def main():
    f = open("input11.txt", "r")
    texts = f.read().split('\n\n')

    monkeys = []
    the_monkeys = []
    for text in texts:
        monkeys.append(Monkey(text))
        the_monkeys.append(Monkey(text))

    for n in range(20):
        for monkey in monkeys:
            monkey.run_operation()
            monkey.relief()
            monkey.test(monkeys)
            pass
        pass

    values = []
    for monkey in monkeys:
        values.append(monkey.observations)
        print(monkey.observations)

    value1 = max(values)
    values.remove(value1)
    value2 = max(values)
    monkey_business = value1*value2
    print(monkey_business)

    for n in range(20):
        comparisons = ''
        for monkey in the_monkeys:
            comparisons += f'{len(monkey.items)} '
            monkey.run_operation()
            monkey.test(the_monkeys)
            pass
        pass
        print(comparisons)


if __name__ == "__main__":
    main()
