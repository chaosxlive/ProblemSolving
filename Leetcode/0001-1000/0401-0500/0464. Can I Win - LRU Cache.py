# https://leetcode.com/problems/can-i-win/

from functools import lru_cache


class Solution:

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False

        @lru_cache(None)
        def solve(chosen: int, rest: int):
            for i in reversed(range(1, maxChoosableInteger + 1)):
                mask = 1 << i
                if chosen & mask:
                    continue
                if rest - i <= 0:
                    return True
                if not solve(chosen | mask, rest - i):
                    return True
            return False

        return solve(0, desiredTotal)
