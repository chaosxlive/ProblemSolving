# https://leetcode.com/problems/cherry-pickup-ii/

from functools import lru_cache
from typing import List


class Solution:

    def cherryPickup(self, grid: List[List[int]]) -> int:
        H = len(grid)
        W = len(grid[0])

        @lru_cache(None)
        def solve(rowIdx: int, rb1Idx: int, rb2Idx: int) -> int:
            curr = grid[rowIdx][rb1Idx] + grid[rowIdx][rb2Idx]
            if rowIdx == H - 1:
                return curr
            maximum = 0
            for dRb1Idx in [-1, 0, 1]:
                nRb1Idx = rb1Idx + dRb1Idx
                if nRb1Idx < 0 or nRb1Idx >= W:
                    continue
                for dRb2Idx in [-1, 0, 1]:
                    nRb2Idx = rb2Idx + dRb2Idx
                    if nRb2Idx < 0 or nRb2Idx >= W:
                        continue
                    if nRb1Idx == nRb2Idx:
                        continue
                    maximum = max(maximum, solve(rowIdx + 1, nRb1Idx, nRb2Idx))
            return curr + maximum

        return solve(0, 0, W - 1)
