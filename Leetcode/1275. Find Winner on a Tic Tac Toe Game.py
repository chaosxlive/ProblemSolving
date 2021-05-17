# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        countARow, countACol, countADiagLT, countADiagRT = [0, 0, 0], [0, 0, 0], 0, 0
        countBRow, countBCol, countBDiagLT, countBDiagRT = [0, 0, 0], [0, 0, 0], 0, 0
        isAMove = True
        for move in moves:
            if isAMove:
                countARow[move[0]] += 1
                if countARow[move[0]] == 3:
                    return 'A'
                countACol[move[1]] += 1
                if countACol[move[1]] == 3:
                    return 'A'
                if move[0] == move[1]:
                    countADiagLT += 1
                    if countADiagLT == 3:
                        return 'A'
                if move[0] + move[1] == 2:
                    countADiagRT += 1
                    if countADiagRT == 3:
                        return 'A'
                isAMove = False
            else:
                countBRow[move[0]] += 1
                if countBRow[move[0]] == 3:
                    return 'B'
                countBCol[move[1]] += 1
                if countBCol[move[1]] == 3:
                    return 'B'
                if move[0] == move[1]:
                    countBDiagLT += 1
                    if countBDiagLT == 3:
                        return 'B'
                if move[0] + move[1] == 2:
                    countBDiagRT += 1
                    if countBDiagRT == 3:
                        return 'B'
                isAMove = True
        return 'Draw' if len(moves) == 9 else 'Pending'