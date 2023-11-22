# https://leetcode.com/problems/paint-house/

from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        prev = [0, 0, 0]
        for c1, c2, c3 in costs:
            prev = [min(prev[1], prev[2]) + c1, min(prev[0], prev[2]) + c2, min(prev[0], prev[1]) + c3]
        return min(prev)
