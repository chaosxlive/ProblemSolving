# https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/

from functools import lru_cache
from typing import List


class Solution:

    def sumOfPower(self, nums: List[int], k: int) -> int:
        if sum(nums) < k:
            return 0
        L = len(nums)
        MOD = 10**9 + 7

        @lru_cache(None)
        def solve(i, target, notPicked):
            if i == L:
                return 1 if target == 0 else 0
            result = solve(i + 1, target, notPicked)
            if nums[i] == target:
                return result + pow(2, notPicked - 1, MOD)
            if nums[i] < target:
                result += solve(i + 1, target - nums[i], notPicked - 1)
            return result % MOD

        return solve(0, k, len(nums)) % MOD
