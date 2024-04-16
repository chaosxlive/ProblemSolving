# https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/

from functools import lru_cache
from math import inf
from typing import List


class Solution:

    def maximumStrength(self, nums: List[int], k: int) -> int:
        L = len(nums)

        @lru_cache(None)
        def solve(i, j, isSub):
            if i == L:
                if j != k:
                    return -inf
                return 0
            result = -inf
            coef = 1 if j % 2 > 0 else -1
            if isSub:
                result = max(result, nums[i] * (k - j + 1) * coef + solve(i + 1, j, True))
            if j != k:
                result = max(result, nums[i] * (k - j) * -coef + solve(i + 1, j + 1, True))
            result = max(result, solve(i + 1, j, False))
            return result

        ret = solve(0, 0, False)
        solve.cache_clear()
        return ret
