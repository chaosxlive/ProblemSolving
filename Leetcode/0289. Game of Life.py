# https://leetcode.com/problems/game-of-life/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0, 1],
            [1, -1], [1, 0], [1, 1]
        ]
        for indexRow in range(len(board)):
            for indexCol in range(len(board[0])):
                count = 0
                for neighbor in neighbors:
                    if 0 <= indexRow + neighbor[0] < len(board) and \
                            0 <= indexCol + neighbor[1] < len(board[0]) and \
                            board[indexRow + neighbor[0]][indexCol + neighbor[1]] & 1 == 1:
                        count += 1
                if board[indexRow][indexCol] == 1:
                    if count == 2 or count == 3:
                        board[indexRow][indexCol] += 2
                elif count == 3:
                    board[indexRow][indexCol] += 2
        for indexRow in range(len(board)):
            for indexCol in range(len(board[0])):
                board[indexRow][indexCol] >>= 1
