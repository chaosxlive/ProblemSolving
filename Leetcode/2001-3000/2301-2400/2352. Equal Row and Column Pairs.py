# https://leetcode.com/problems/equal-row-and-column-pairs/

from typing import List
from collections import defaultdict


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowHashes = defaultdict(int)
        for row in grid:
            rowHashes[tuple(row)] += 1
        result = 0
        for i in range(len(grid[0])):
            col = tuple(grid[j][i] for j in range(len(grid)))
            result += rowHashes[col]
        return result
