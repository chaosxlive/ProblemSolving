# https://leetcode.com/problems/distinct-subsequences/

from functools import lru_cache


class Solution:

    def numDistinct(self, s: str, t: str) -> int:
        LS = len(s)
        LT = len(t)
        if LS < LT:
            return 0

        @lru_cache(None)
        def solve(si, ti):
            if ti == LT:
                return 1
            if si == LS:
                return 0
            result = 0
            if s[si] == t[ti]:
                result += solve(si + 1, ti + 1)
            result += solve(si + 1, ti)
            return result

        return solve(0, 0)
