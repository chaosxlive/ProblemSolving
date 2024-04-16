# https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/

from math import ceil, inf


class Solution:

    def minOperations(self, k: int) -> int:
        res = inf
        i = 0
        while i < k:
            n = 1 + i
            res = min(res, i if n >= k else (i + ceil(k / n) - 1))
            i += 1
        return res
