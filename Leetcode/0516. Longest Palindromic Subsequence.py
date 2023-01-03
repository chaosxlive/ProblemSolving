# https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        for i in range(len(s) - 1, -1, -1):
            leftTop = 0
            for j in range(len(s)):
                if s[j] == s[i]:
                    dp[j + 1], leftTop = leftTop + 1, dp[j + 1]
                else:
                    dp[j + 1], leftTop = max(dp[j], dp[j + 1]), dp[j + 1]
        return dp[-1]
