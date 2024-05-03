# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/

MOD = 10**9 + 7


class Solution:

    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        LIMIT = limit + 1

        MEMO = [[[-1, -1] for o in range(one + 1)] for z in range(zero + 1)]

        def solve(z, o, v):
            if MEMO[z][o][v] != -1:
                return MEMO[z][o][v]
            n = z + o
            if z == 0 or o == 0:
                if n >= LIMIT:
                    MEMO[z][o][v] = 0
                elif z == 0 and v == 0:
                    MEMO[z][o][v] = 0
                elif o == 0 and v == 1:
                    MEMO[z][o][v] = 0
                else:
                    MEMO[z][o][v] = 1
                return MEMO[z][o][v]
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
            MEMO[z][o][v] = (pickZero + pickOne) % MOD
            return MEMO[z][o][v]

        return (solve(zero, one, 0) + solve(zero, one, 1)) % MOD
