# https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        safe = set()

        def inBound(board, row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def markSafe(board, safe, row, col):
            if not inBound(board, row, col) or (row, col) in safe or board[row][col] == 'X':
                return

            safe.add((row, col))

            for r, c in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                markSafe(board, safe, row + r, col + c)

        for row in range(len(board)):
            if board[row][0] == 'X':
                safe.add((row, 0))
            else:
                markSafe(board, safe, row, 0)
            if board[row][len(board[0]) - 1] == 'X':
                safe.add((row, len(board[0]) - 1))
            else:
                markSafe(board, safe, row, len(board[0]) - 1)
        for col in range(len(board[0])):
            if board[0][col] == 'X':
                safe.add((0, col))
            else:
                markSafe(board, safe, 0, col)
            if board[len(board) - 1][col] == 'X':
                safe.add((len(board) - 1, col))
            else:
                markSafe(board, safe, len(board) - 1, col)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row, col) in safe or board[row][col] == 'X':
                    continue
                board[row][col] = 'X'
