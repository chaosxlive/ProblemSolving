# https://leetcode.com/problems/make-array-strictly-increasing/

from bisect import bisect_right
from functools import lru_cache
from math import inf
from typing import List


class Solution:

    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = [-1] + arr1
        arr2 = sorted(set(arr2))
        L1 = len(arr1)
        L2 = len(arr2)

        @lru_cache(None)
        def solve(i, iPrev):
            if i == L1:
                return 0
            res = inf
            n = arr1[i]
            prev = arr1[i - 1] if iPrev == -1 else arr2[iPrev]
            if n > prev:
                res = min(res, solve(i + 1, -1))
            j = bisect_right(arr2, prev)
            if j < L2:
                res = min(res, solve(i + 1, j) + 1)
            return res

        result = min(solve(1, i) + (1 if i >= 0 else 0) for i in range(-1, L2))
        return -1 if result == inf else result
