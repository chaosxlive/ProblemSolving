# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

from typing import List


class Solution:

    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        s = [[0] * len(grid[0]) for _ in range(len(grid))]
        s[0][0] = grid[0][0]
        result = 1 if s[0][0] <= k else 0
        for i in range(1, len(grid)):
            s[i][0] = s[i - 1][0] + grid[i][0]
            if s[i][0] <= k:
                result += 1
        for i in range(1, len(grid[0])):
            s[0][i] = s[0][i - 1] + grid[0][i]
            if s[0][i] <= k:
                result += 1
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + grid[i][j]
                if s[i][j] <= k:
                    result += 1
        return result
