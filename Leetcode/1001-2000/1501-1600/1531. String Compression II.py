# https://leetcode.com/problems/string-compression-ii/

from functools import lru_cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        L = len(s)

        @lru_cache(None)
        def solve(idx: int, prev: str, prevCnt: int, rest: int):
            if rest < 0:
                return 2147483647
            if idx == L:
                return 0
            result = solve(idx + 1, prev, prevCnt, rest - 1)
            if s[idx] == prev:
                result = min(result, solve(idx + 1, prev, prevCnt + 1, rest) + (1 if prevCnt in [1, 9, 99] else 0))
            else:
                result = min(result, solve(idx + 1, s[idx], 1, rest) + 1)
            return result

        return solve(0, '', 0, k)
