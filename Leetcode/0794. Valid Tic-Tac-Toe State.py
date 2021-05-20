# https://leetcode.com/problems/valid-tic-tac-toe-state/

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        # countRowO, countColO, countRTO, countLTO, countRowX, countColX, countRTX, countLTX
        # =
        #       0~2,       3~5,        6,        7,      8~10,     11~13,       14,       15
        counts, countO, countX = [0] * 16, 0, 0
        for indexRow in range(3):
            for indexCol in range(3):
                if board[indexRow][indexCol] == 'O':
                    countO += 1
                    counts[0 + indexRow] += 1
                    counts[3 + indexCol] += 1
                    if indexRow == indexCol:
                        counts[6] += 1
                    if indexRow + indexCol == 2:
                        counts[7] += 1
                if board[indexRow][indexCol] == 'X':
                    countX += 1
                    counts[8 + indexRow] += 1
                    counts[11 + indexCol] += 1
                    if indexRow == indexCol:
                        counts[14] += 1
                    if indexRow + indexCol == 2:
                        counts[15] += 1
        if countX - countO != 1 and countX - countO != 0:
            return False
        isXEnd = False
        for c in counts[8:]:
            if c == 3:
                isXEnd = True
        if isXEnd and countX - countO == 0:
            return False
        isOEnd = False
        for c in counts[:8]:
            if c == 3:
                isOEnd = True
        if isOEnd and countX - countO == 1:
            return False
        return True
