# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

from functools import lru_cache
from typing import List


class Solution:

    def maxProfit(self, k: int, prices: List[int]) -> int:
        L = len(prices)

        @lru_cache(None)
        def solve(i, rest, isHold):
            if i == L or rest == 0:
                return 0
            res = solve(i + 1, rest, isHold)
            if isHold:
                res = max(res, solve(i + 1, rest - 1, False) + prices[i])
            else:
                res = max(res, solve(i + 1, rest, True) - prices[i])
            return res

        res = solve(0, min(k, L // 2), False)
        return res
