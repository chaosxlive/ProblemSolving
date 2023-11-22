# https://leetcode.com/problems/minimum-path-sum/

from typing import List
from itertools import accumulate


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = list(accumulate(grid[0]))
        for row in range(1, len(grid)):
            dp[0] += grid[row][0]
            for col in range(1, len(grid[0])):
                dp[col] = min(dp[col], dp[col - 1]) + grid[row][col]
        return dp[-1]
