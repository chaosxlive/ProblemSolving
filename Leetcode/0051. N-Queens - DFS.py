# https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.chess = [''] * (n * n)
        self.countRow = [False] * n
        self.countCol = [False] * n
        self.countRT = [False] * (n * 2)
        self.countLT = [False] * (n * 2)
        self.result = []

        self.dfs(0, 0, 0)

        return self.result

    def dfs(self, row, col, count):
        if col == self.n:
            col = 0
            row += 1
        if row == self.n:
            if count == self.n:
                temp = []
                for row in range(self.n):
                    temp.append("".join(self.chess[self.n * row: self.n * (row + 1)]))
                self.result.append(temp)
            return

        if not self.countRow[row] and not self.countCol[col] and not self.countRT[col - row + self.n] and not self.countLT[row + col]:
            self.chess[self.n * row + col] = 'Q'
            self.countRow[row] = True
            self.countCol[col] = True
            self.countRT[col - row + self.n] = True
            self.countLT[row + col] = True
            self.dfs(row, col + 1, count + 1)
            self.countRow[row] = False
            self.countCol[col] = False
            self.countRT[col - row + self.n] = False
            self.countLT[row + col] = False
        self.chess[self.n * row + col] = '.'
        self.dfs(row, col + 1, count)
