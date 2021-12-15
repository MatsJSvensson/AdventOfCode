import math

def main():
    f = open("input4.txt", "r")
    input = f.readlines()
    f.close()

    clouds = {}

    for line in input:
        if len(line) > 1:
            start, end = line.split(' -> ')
            x1, y1 = start.split(',')
            x2, y2 = end.split(',')
            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)
            y2 = int(y2)

            if x1 == x2:
                if y1 < y2:
                    diff = y2 - y1 + 1
                    y_start = y1
                else:
                    diff = y1 - y2 + 1
                    y_start = y2
                for n in range(0, diff):
                    name = str(x1) + ',' + str(y_start + n)
                    if name in clouds.keys():
                        clouds[name] += 1
                    else:
                        clouds[name] = 1
            if y1 == y2:
                if x1 < x2:
                    diff = x2 - x1 + 1
                    x_start = x1
                else:
                    diff = x1 - x2 + 1
                    x_start = x2
                for n in range(0, diff):
                    name = str(x_start + n) + ',' + str(y1)
                    if name in clouds.keys():
                        clouds[name] += 1
                    else:
                        clouds[name] = 1

    amount = 0
    for point in clouds.values():
        if point > 1:
            amount += 1

    print(f'amount: {amount}')


    for line in input:
        if len(line) > 1:
            start, end = line.split(' -> ')
            x1, y1 = start.split(',')
            x2, y2 = end.split(',')
            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)
            y2 = int(y2)

            if y1 < y2:
                y_diff = y2 - y1 + 1
                y_dir = 1
            else:
                y_diff = y1 - y2 + 1
                y_dir = -1
            if x1 < x2:
                x_diff = x2 - x1 + 1
                x_dir = 1
            else:
                x_diff = x1 - x2 + 1
                x_dir = -1
            if x_diff == y_diff:

                for n in range(0, x_diff):
                    name = str(x1 + n*x_dir) + ',' + str(y1 + n*y_dir)
                    if name in clouds.keys():
                        clouds[name] += 1
                    else:
                        clouds[name] = 1

    amount = 0
    for point in clouds.values():
        if point > 1:
            amount += 1

    print(f'amount: {amount}')


if __name__ == '__main__':
    main()