# https://leetcode.com/problems/beautiful-arrangement/

from functools import lru_cache


class Solution:

    def countArrangement(self, n: int) -> int:

        @lru_cache(None)
        def solve(unuseds:int, pos:int):
            if pos == n + 1:
                return 1
            i = pos
            result = 0
            for j in range(1, n + 1):
                bit = 1 << (j - 1)
                if bit & unuseds > 0:
                    continue
                if i % j > 0 and j % i > 0:
                    continue
                result += solve(unuseds | bit, pos + 1)
            return result

        return solve(0, 1)
