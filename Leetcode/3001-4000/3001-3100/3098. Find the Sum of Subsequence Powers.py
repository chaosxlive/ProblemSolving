# https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

from functools import lru_cache
from math import inf
from typing import List


class Solution:

    def sumOfPowers(self, nums: List[int], k: int) -> int:
        L = len(nums)
        MOD = 10**9 + 7
        nums.sort()

        @lru_cache(None)
        def dfs(i, prev, diff, cnt):
            if cnt == k:
                return diff
            if i == L:
                return 0
            res = 0
            # Not take
            res += dfs(i + 1, prev, diff, cnt)
            # Take
            res += dfs(i + 1, i, diff if prev == -1 else min(diff, nums[i] - nums[prev]), cnt + 1)
            return res % MOD

        return dfs(0, -1, inf, 0)
