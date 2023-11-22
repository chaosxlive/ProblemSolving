# https://leetcode.com/problems/out-of-boundary-paths/

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        MOD_BASE = 1000000007

        def isInBound(m, n, row, col):
            return 0 <= row < m and 0 <= col < n

        dp = [[[0 for move in range(maxMove + 1)] for col in range(n)] for row in range(m)]

        for move in range(1, maxMove + 1):
            for row in range(m):
                for col in range(n):
                    for dir in dirs:
                        if not isInBound(m, n, row + dir[0], col + dir[1]):
                            dp[row][col][move] += 1
                        else:
                            dp[row][col][move] += dp[row + dir[0]][col + dir[1]][move - 1] % MOD_BASE
        return dp[startRow][startColumn][maxMove] % MOD_BASE
