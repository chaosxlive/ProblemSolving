# https://www.codewars.com/kata/529bf0e9bdf7657179000008/train/python

def valid_solution(board):
    rowCheck = [set() for row in range(9)]
    colCheck = [set() for col in range(9)]
    blockCheck = [set() for block in range(9)]

    for row in range(9):
        for col in range(9):
            num = board[row][col]
            if num == '0':
                continue

            if num in rowCheck[row]:
                return False
            rowCheck[row].add(num)

            if num in colCheck[col]:
                return False
            colCheck[col].add(num)

            if num in blockCheck[(row // 3) * 3 + (col // 3)]:
                return False
            blockCheck[(row // 3) * 3 + (col // 3)].add(num)
    return True