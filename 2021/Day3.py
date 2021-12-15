
def main():
    f = open("input3.txt", "r")
    input = f.readlines()
    f.close()

    numbers = input[0].strip().split(',')
    boards = []
    temp_list = []
    for n in range(2,len(input)):
        if len(input[n]) > 1:
            row = input[n].replace('  ', ' ').strip()
            row = row.split(' ')
            temp_list.append(row)
        else:
            boards.append(temp_list.copy())
            temp_list.clear()

    the_sum = 0
    the_product = 0
    for n in numbers:
        for board in boards:
            for line in board:
                for x in range(5):
                    if line[x] == n:
                        line[x] = 'x'

        for board in boards:
            rows = [0,0,0,0,0]
            columns = [0,0,0,0,0]
            board_sum = 0
            for x in range(5):
                for y in range(5):
                    if board[x][y] == 'x':
                        rows[x] += 1
                        columns[y] += 1
                    else:
                        board_sum += int(board[x][y])
            if 5 in rows or 5 in columns:
                the_sum = board_sum
                print(board)
                print(f'sum: {the_sum}')
                break

        if the_sum > 0:
            the_product = int(n) * the_sum
            break
    print(f'product: {the_product}')

    the_sum = 0
    the_product = 0
    for n in numbers:
        new_boards = []
        last_board = []
        for board in boards:
            for line in board:
                for x in range(5):
                    if line[x] == n:
                        line[x] = 'x'

        for board in boards:
            rows = [0,0,0,0,0]
            columns = [0,0,0,0,0]
            board_sum = 0
            for x in range(5):
                for y in range(5):
                    if board[x][y] == 'x':
                        rows[x] += 1
                        columns[y] += 1
                    else:
                        board_sum += int(board[x][y])
            if 5 in rows or 5 in columns:
                the_sum = board_sum
                last_board = board
            else:
                new_boards.append(board)

        if len(new_boards) == 0:
            the_product = int(n) * the_sum
            print(last_board)
            print(f'sum: {the_sum}')
            break

        boards = new_boards
    print(f'product: {the_product}')


if __name__ == '__main__':
    main()