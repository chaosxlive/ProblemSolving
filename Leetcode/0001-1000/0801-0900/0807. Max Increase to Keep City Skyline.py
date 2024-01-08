# https://leetcode.com/problems/max-increase-to-keep-city-skyline/

from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        L = len(grid)
        maxR = [0] * L
        maxC = [0] * L
        for r, R in enumerate(grid):
            for c, C in enumerate(R):
                maxR[r] = max(maxR[r], C)
                maxC[c] = max(maxC[c], C)
        result = 0
        for r, R in enumerate(grid):
            for c, C in enumerate(R):
                result += min(maxR[r], maxC[c]) - C
        return result
