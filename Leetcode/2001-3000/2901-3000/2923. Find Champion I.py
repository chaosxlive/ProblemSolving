# https://leetcode.com/problems/find-champion-i/

from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i, res in enumerate(grid):
            if sum(res) == n - 1:
                return i
        return -1
