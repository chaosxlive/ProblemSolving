# https://leetcode.com/problems/minimum-falling-path-sum/

from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = matrix[0][:]
        for i in range(1, len(matrix)):
            temp = dp[:]
            for j in range(len(matrix[0])):
                topLeft = dp[j - 1] if j > 0 else dp[j]
                topCenter = dp[j]
                topRight = dp[j + 1] if j < len(matrix) - 1 else dp[j]
                temp[j] = min(topLeft, topCenter, topRight) + matrix[i][j]
            dp = temp
        return min(dp)
