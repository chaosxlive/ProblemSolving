# https://leetcode.com/problems/paint-house-ii/

from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        prev = [0] * len(costs[0])
        for cost in costs:
            prev = [min(prev[:i] + prev[i + 1:]) + cost[i] for i in range(len(costs[0]))]
        return min(prev)
