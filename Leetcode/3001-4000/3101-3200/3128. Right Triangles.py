# https://leetcode.com/problems/right-triangles/

from typing import List


class Solution:

    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        res = 0
        rowCnt = [0] * len(grid)
        colCnt = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rowCnt[i] += 1
                    colCnt[j] += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += (rowCnt[i] - 1) * (colCnt[j] - 1)
        return res
