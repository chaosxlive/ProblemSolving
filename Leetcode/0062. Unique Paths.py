# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board = [[1 for col in range(n)] for row in range(m)]
        
        for row in range(1, m):
            for col in range(1, n):
                board[row][col] = board[row - 1][col] + board[row][col - 1]
        
        return board[m - 1][n - 1]