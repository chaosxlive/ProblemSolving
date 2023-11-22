# https://leetcode.com/problems/sudoku-solver/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.rowCheck = [set() for row in range(9)]
        self.colCheck = [set() for col in range(9)]
        self.blockCheck = [set() for block in range(9)]

        for row in range(9):
            for col in range(9):
                if self.board[row][col] != '.':
                    self.rowCheck[row].add(ord(self.board[row][col]) - 48)
                    self.colCheck[col].add(ord(self.board[row][col]) - 48)
                    self.blockCheck[(row // 3) * 3 + (col // 3)].add(ord(self.board[row][col]) - 48)

        self.solve(0, 0)

    def solve(self, row, col):
        if col == 9:
            row += 1
            col = 0
        if row == 9:
            return True
        while self.board[row][col] != '.':
            col += 1
            if col == 9:
                row += 1
                col = 0
            if row == 9:
                return True
        for num in range(1, 10):
            if num in self.rowCheck[row] or \
               num in self.colCheck[col] or \
               num in self.blockCheck[(row // 3) * 3 + (col // 3)]:
                continue
            self.rowCheck[row].add(num)
            self.colCheck[col].add(num)
            self.blockCheck[(row // 3) * 3 + (col // 3)].add(num)
            self.board[row][col] = str(num)
            if self.solve(row, col + 1):
                return True

            self.rowCheck[row].remove(num)
            self.colCheck[col].remove(num)
            self.blockCheck[(row // 3) * 3 + (col // 3)].remove(num)
            self.board[row][col] = '.'
        return False
