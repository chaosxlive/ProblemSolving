# https://leetcode.com/problems/largest-1-bordered-square/

from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        bottoms = [[0] * len(grid[0]) for _ in range(len(grid))]
        rights = [[0] * len(grid[0]) for _ in range(len(grid))]
        for r in range(len(grid)):
            ic = len(grid[0]) - 1
            count = 0
            while ic >= 0:
                if grid[r][ic] == 1:
                    count += 1
                else:
                    count = 0
                rights[r][ic] = count
                ic -= 1
        for c in range(len(grid[0])):
            ir = len(grid) - 1
            count = 0
            while ir >= 0:
                if grid[ir][c] == 1:
                    count += 1
                else:
                    count = 0
                bottoms[ir][c] = count
                ir -= 1

        for l in range(min(len(grid), len(grid[0])), 0, -1):
            for r in range(len(grid) - l + 1):
                for c in range(len(grid[0]) - l + 1):
                    if bottoms[r][c] >= l and \
                            rights[r][c] >= l and \
                            bottoms[r][c + l - 1] >= l and \
                            rights[r+l - 1][c] >= l:
                        return l * l
        return 0
