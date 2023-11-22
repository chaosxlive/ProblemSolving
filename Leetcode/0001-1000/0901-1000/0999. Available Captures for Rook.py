# https://leetcode.com/problems/available-captures-for-rook/

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rookRow = 0
        while rookRow < len(board):
            rookCol = 0
            isFound = False
            while rookCol < len(board[0]):
                if board[rookRow][rookCol] == 'R':
                    isFound = True
                    break
                rookCol += 1
            if isFound:
                break
            rookRow += 1

        result = 0
        row = rookRow + 1
        while row < len(board):
            if board[row][rookCol] != '.':
                if board[row][rookCol] == 'p':
                    result += 1
                break
            row += 1
        row = rookRow - 1
        while row >= 0:
            if board[row][rookCol] != '.':
                if board[row][rookCol] == 'p':
                    result += 1
                break
            row -= 1
        col = rookCol + 1
        while col < len(board[0]):
            if board[rookRow][col] != '.':
                if board[rookRow][col] == 'p':
                    result += 1
                break
            col += 1
        col = rookCol - 1
        while col >= 0:
            if board[rookRow][col] != '.':
                if board[rookRow][col] == 'p':
                    result += 1
                break
            col -= 1

        return result
