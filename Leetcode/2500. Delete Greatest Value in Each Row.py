# https://leetcode.com/problems/delete-greatest-value-in-each-row/

from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        return sum(map(max, zip(*[sorted(row) for row in grid])))
