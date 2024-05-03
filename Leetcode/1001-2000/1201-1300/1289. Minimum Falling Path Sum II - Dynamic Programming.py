# https://leetcode.com/problems/minimum-falling-path-sum-ii/

from math import inf
from typing import List


class Solution:

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        L = len(grid)
        if L == 1:
            return grid[0][0]
        dp = [0] * (L + 2)
        dp[0] = inf
        dp[-1] = inf
        for row in grid:
            dpTemp = dp[:]
            for i, C in enumerate(row):
                dpTemp[i + 1] = min(dp[j + 1] for j, c in enumerate(row) if i != j) + C
            dp = dpTemp
        return min(dp)
