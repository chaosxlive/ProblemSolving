from functools import lru_cache
from typing import List, Optional


class Solution:

    def sumOfPower(self, nums: List[int], k: int) -> int:
        if sum(nums) < k:
            return 0
        L = len(nums)
        MOD = 10**9 + 7

        @lru_cache(None)
        def solve(i, target, ignoredCnt):
            if i == L:
                if target == 0:
                    return 1
                return 0
            result = solve(i + 1, target, ignoredCnt + 1)
            if nums[i] == target:
                # print('A')
                # print(pow(2, ignoredCnt + L - i - 1, MOD))
                return result + pow(2, ignoredCnt + L - i - 1, MOD)
            # print('B')
            # print(solve(i + 1, target, ignoredCnt + 1))
            if nums[i] < target:
                # print('C')
                # print(solve(i + 1, target - nums[i], ignoredCnt))
                result += solve(i + 1, target - nums[i], ignoredCnt)
            return result % MOD

        return solve(0, k, 0) % MOD


#
# print(Solution().sumOfPower([2, 3, 3], 5))
