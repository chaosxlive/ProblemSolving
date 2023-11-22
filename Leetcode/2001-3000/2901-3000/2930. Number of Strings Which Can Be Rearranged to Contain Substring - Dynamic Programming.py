# https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/

from functools import lru_cache


MOD = 1000000007


class Solution:
    def stringCount(self, n: int) -> int:

        @lru_cache(None)
        def solve(cntN, cntL, cntE, cntT):
            if cntN == 0:
                if cntL == 0 and cntE == 0 and cntT == 0:
                    return 1
                return 0
            result = 23 * solve(cntN - 1, cntL, cntE, cntT)
            if cntL > 0:
                result += solve(cntN - 1, cntL - 1, cntE, cntT)
            else:
                result += solve(cntN - 1, cntL, cntE, cntT)
            if cntE > 0:
                result += solve(cntN - 1, cntL, cntE - 1, cntT)
            else:
                result += solve(cntN - 1, cntL, cntE, cntT)
            if cntT > 0:
                result += solve(cntN - 1, cntL, cntE, cntT - 1)
            else:
                result += solve(cntN - 1, cntL, cntE, cntT)
            return result % MOD

        return solve(n, 1, 2, 1) % MOD
