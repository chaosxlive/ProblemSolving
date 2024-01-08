# https://leetcode.com/problems/number-of-self-divisible-permutations/

from functools import lru_cache
from math import gcd


class Solution:
    def selfDivisiblePermutationCount(self, n: int) -> int:
        isValid = [[True] * 13] + [[True] + [gcd(i, pos) == 1 for i in range(1, 13)] for pos in range(1, 13)]

        @lru_cache(None)
        def solve(setMask: int, pos: int):
            return 1 if pos == n else sum(solve(setMask | (1 << i), pos + 1) for i in range(1, n + 1) if isValid[pos + 1][i] if not (1 << i) & setMask)

        return solve(0, 0)
