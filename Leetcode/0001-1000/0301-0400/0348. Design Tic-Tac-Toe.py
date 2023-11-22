# https://leetcode.com/problems/design-tic-tac-toe/

class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rowCnt1 = [0] * n
        self.colCnt1 = [0] * n
        self.diagCnt1 = [0, 0]
        self.rowCnt2 = [0] * n
        self.colCnt2 = [0] * n
        self.diagCnt2 = [0, 0]

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.rowCnt1[row] += 1
            if self.rowCnt1[row] == self.n:
                return 1
            self.colCnt1[col] += 1
            if self.colCnt1[col] == self.n:
                return 1
            if row == col:
                self.diagCnt1[0] += 1
                if self.diagCnt1[0] == self.n:
                    return 1
            if row + col == self.n - 1:
                self.diagCnt1[1] += 1
                if self.diagCnt1[1] == self.n:
                    return 1
        else:
            self.rowCnt2[row] += 1
            if self.rowCnt2[row] == self.n:
                return 2
            self.colCnt2[col] += 1
            if self.colCnt2[col] == self.n:
                return 2
            if row == col:
                self.diagCnt2[0] += 1
                if self.diagCnt2[0] == self.n:
                    return 2
            if row + col == self.n - 1:
                self.diagCnt2[1] += 1
                if self.diagCnt2[1] == self.n:
                    return 2
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
