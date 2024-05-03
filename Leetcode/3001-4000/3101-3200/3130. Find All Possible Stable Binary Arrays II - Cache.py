# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/

from functools import cache

MOD = 10**9 + 7


class Solution:

    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        LIMIT = limit + 1

        @cache
        def solve(z, o, v):
            n = z + o
            if z == 0 or o == 0:
                if n >= LIMIT:
                    return 0
                elif z == 0 and v == 0:
                    return 0
                elif o == 0 and v == 1:
                    return 0
                else:
                    return 1
            if v == 0:
                pickZero = solve(z - 1, o, 0)
                if z >= LIMIT:
                    pickZero -= solve(z - LIMIT, o, 1)
                pickOne = solve(z - 1, o, 1)
            else:
                pickZero = solve(z, o - 1, 0)
                pickOne = solve(z, o - 1, 1)
                if o >= LIMIT:
                    pickOne -= solve(z, o - LIMIT, 0)
            return (pickZero + pickOne) % MOD

        res = (solve(zero, one, 0) + solve(zero, one, 1)) % MOD
        solve.cache_clear()
        return res
