# https://leetcode.com/problems/make-a-square-with-the-same-color/

from typing import List


class Solution:

    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i in range(2):
            for j in range(2):
                if (grid[i][j] == 'B') + (grid[i + 1][j] == 'B') + (grid[i][j + 1] == 'B') + (grid[i + 1][j + 1] == 'B') != 2:
                    return True
        return False
