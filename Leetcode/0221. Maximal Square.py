# https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]
        result = 0
        for indexRow in range(len(matrix)):
            for indexCol in range(len(matrix[0])):
                if matrix[indexRow][indexCol] == '0':
                    continue
                dp[indexRow][indexCol] = min(dp[indexRow - 1][indexCol], dp[indexRow - 1][indexCol - 1], dp[indexRow][indexCol - 1]) + 1
                if dp[indexRow][indexCol] > result:
                    result = dp[indexRow][indexCol]
        return result * result
