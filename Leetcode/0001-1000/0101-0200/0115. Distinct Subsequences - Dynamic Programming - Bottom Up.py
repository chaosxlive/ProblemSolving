# https://leetcode.com/problems/distinct-subsequences/


class Solution:

    def numDistinct(self, s: str, t: str) -> int:
        LS = len(s)
        LT = len(t)
        if LS < LT:
            return 0

        dp = [0] * (LT + 1)
        for si in reversed(range(LS)):
            prev = 1
            for ti in reversed(range(LT)):
                if s[si] == t[ti]:
                    dp[ti], prev = dp[ti] + prev, dp[ti]
                else:
                    prev = dp[ti]
        return dp[0]
