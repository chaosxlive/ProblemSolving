# https://leetcode.com/problems/minimum-number-of-coins-for-fruits/

from functools import lru_cache
from typing import List


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:

        @lru_cache(None)
        def solve(currIdx, freeIdx):
            if currIdx == len(prices):
                return 0
            cost = solve(currIdx + 1, 2 * currIdx + 1) + prices[currIdx]
            if currIdx <= freeIdx:
                cost = min(cost, solve(currIdx + 1, freeIdx))
            return cost

        return solve(0, -1)
