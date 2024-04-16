# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

from functools import lru_cache
from typing import List, Tuple


class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:

        @lru_cache(None)
        def solve(left: int, right: int, restCuts: Tuple[int]) -> int:
            if len(restCuts) == 0:
                return 0
            result = 2147483647
            for i, cut in enumerate(restCuts):
                result = min(result, solve(left, cut, tuple(restCuts[:i])) + solve(cut, right, tuple(restCuts[i + 1:])))
            return result + right - left

        return solve(0, n, tuple(sorted(cuts)))
