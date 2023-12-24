# https://leetcode.com/problems/best-meeting-point/

from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rs = []
        cs = []
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == 1:
                    rs.append(r)
                    cs.append(c)
        rs.sort()
        cs.sort()
        mr = rs[len(rs) // 2]
        mc = cs[len(cs) // 2]

        result = 0
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == 1:
                    result += abs(r - mr) + abs(c - mc)
        return result
