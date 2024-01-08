# https://leetcode.com/problems/max-increase-to-keep-city-skyline/

from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        maxR = [max(row) for row in grid]
        maxC = [max(col) for col in zip(*grid)]
        return sum(min(maxR[r], maxC[c]) - C for r, R in enumerate(grid) for c, C in enumerate(R))
