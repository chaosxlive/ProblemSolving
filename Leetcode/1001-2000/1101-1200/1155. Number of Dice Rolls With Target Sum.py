# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

from functools import lru_cache

MOD = 10**9+7


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n * k < target or n > target:
            return 0

        @lru_cache(None)
        def solve(cnt: int, t: int):
            if cnt == 0:
                return 1 if cnt == t else 0
            return sum(solve(cnt - 1, t - i) for i in range(1, k + 1)) % MOD

        return solve(n, target)
