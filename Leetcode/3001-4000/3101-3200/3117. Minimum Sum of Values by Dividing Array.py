# https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/

from functools import lru_cache
from math import inf
from typing import List


class Solution:

    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        LN = len(nums)
        LA = len(andValues)

        @lru_cache(None)
        def solve(startIdx, prevAnds, andIdx):
            if startIdx == LN and andIdx == LA:
                return 0
            elif startIdx == LN or andIdx == LA:
                return inf
            prevAnds &= nums[startIdx]
            if prevAnds < andValues[andIdx]:
                return inf
            res = solve(startIdx + 1, prevAnds, andIdx)
            if prevAnds > andValues[andIdx]:
                return res
            return min(res, solve(startIdx + 1, -1, andIdx + 1) + nums[startIdx])

        result = solve(0, -1, 0)
        return -1 if result == inf else result
