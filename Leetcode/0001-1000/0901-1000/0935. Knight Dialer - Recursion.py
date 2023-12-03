# https://leetcode.com/problems/knight-dialer/

from functools import lru_cache

MOD = 10**9 + 7


class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        @lru_cache(None)
        def solve(step, pos):
            if step == 1:
                return 1
            if pos == 1:
                return (solve(step-1, 6) + solve(step-1, 8)) % MOD
            if pos == 2:
                return (solve(step-1, 7) + solve(step-1, 9)) % MOD
            if pos == 3:
                return (solve(step-1, 4) + solve(step-1, 8)) % MOD
            if pos == 4:
                return (solve(step-1, 3) + solve(step-1, 9) + solve(step-1, 0)) % MOD
            if pos == 6:
                return (solve(step-1, 1) + solve(step-1, 7) + solve(step-1, 0)) % MOD
            if pos == 7:
                return (solve(step-1, 2) + solve(step-1, 6)) % MOD
            if pos == 8:
                return (solve(step-1, 1) + solve(step-1, 3)) % MOD
            if pos == 9:
                return (solve(step-1, 2) + solve(step-1, 4)) % MOD
            if pos == 0:
                return (solve(step-1, 4) + solve(step-1, 6)) % MOD

        result = 0
        for i in range(10):
            if i == 5:
                continue
            result += solve(n, i)
        return result % MOD
