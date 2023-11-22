# https://leetcode.com/problems/n-queens/

class Solution:
    def totalNQueens(self, n: int) -> int:
        self.n = n
        self.countRow = [False] * n
        self.countCol = [False] * n
        self.countRT = [False] * (n * 2)
        self.countLT = [False] * (n * 2)
        self.result = 0

        self.backtrack(0)

        return self.result

    def backtrack(self, row):
        if row == self.n:
            self.result += 1
            return

        for col in range(self.n):
            if not self.countRow[row] and not self.countCol[col] and not self.countRT[col - row + self.n] and not self.countLT[row + col]:
                self.countRow[row] = True
                self.countCol[col] = True
                self.countRT[col - row + self.n] = True
                self.countLT[row + col] = True
                self.backtrack(row + 1)
                self.countRow[row] = False
                self.countCol[col] = False
                self.countRT[col - row + self.n] = False
                self.countLT[row + col] = False
