# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text1) + 1)
        for c2 in text2:
            leftTop = 0
            for i, c1 in enumerate(text1):
                if c1 == c2:
                    dp[i + 1], leftTop = leftTop + 1, dp[i + 1]
                else:
                    dp[i + 1], leftTop = max(dp[i], dp[i + 1]), dp[i + 1]
        return dp[-1]
