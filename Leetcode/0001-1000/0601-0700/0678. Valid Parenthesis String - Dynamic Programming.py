# https://leetcode.com/problems/valid-parenthesis-string/

from functools import lru_cache


class Solution:

    def checkValidString(self, s: str) -> bool:
        L = len(s)

        @lru_cache(None)
        def solve(i, cnt):
            if i == L:
                return cnt == 0
            if s[i] == '(':
                return solve(i + 1, cnt + 1)
            if s[i] == ')':
                if cnt == 0:
                    return False
                return solve(i + 1, cnt - 1)
            return solve(i + 1, cnt + 1) or (cnt > 0 and solve(i + 1, cnt - 1)) or solve(i + 1, cnt)

        return solve(0, 0)
