# https://leetcode.com/problems/ones-and-zeroes/

from functools import lru_cache
from typing import List


class Solution:

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cnts = [(s.count('0'), s.count('1')) for s in strs]

        @lru_cache(None)
        def solve(i: int, rm: int, rn: int):
            if i == len(strs):
                return 0
            cm, cn = cnts[i]
            result = solve(i + 1, rm, rn)
            if cm <= rm and cn <= rn:
                result = max(result, solve(i + 1, rm - cm, rn - cn) + 1)
            return result

        return solve(0, m, n)
