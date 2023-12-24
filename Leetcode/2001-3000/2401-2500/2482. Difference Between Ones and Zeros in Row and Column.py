# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rs = len(grid)
        cs = len(grid[0])
        rCnt = [0] * rs
        cCnt = [0] * cs
        for r in range(rs):
            for c in range(cs):
                if grid[r][c] == 1:
                    rCnt[r] += 1
                    cCnt[c] += 1
        result = [[0] * cs for _ in range(rs)]
        for r in range(rs):
            for c in range(cs):
                result[r][c] = (rCnt[r] + cCnt[c]) * 2 - (rs + cs)
        return result
