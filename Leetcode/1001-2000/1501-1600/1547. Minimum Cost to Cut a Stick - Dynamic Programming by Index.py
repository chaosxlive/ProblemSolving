# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

from functools import lru_cache
from typing import List


class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()

        @lru_cache(None)
        def solve(left: int, right: int, cutLeft: int, cutRight: int) -> int:
            if cutRight - cutLeft == 0:
                return 0
            result = 2147483647
            for i in range(cutLeft, cutRight):
                cut = cuts[i]
                result = min(result, solve(left, cut, cutLeft, i) + solve(cut, right, i + 1, cutRight))
            return result + right - left

        return solve(0, n, 0, len(cuts))
