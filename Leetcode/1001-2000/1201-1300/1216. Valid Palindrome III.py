# https://leetcode.com/problems/valid-palindrome-iii/

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        l = len(s)
        dp = [[0] * (l + 1) for i in range(l + 1)]
        for i in range(l + 1):
            dp[0][i] = dp[i][0] = i
        for i in range(1, l + 1):
            for j in range(1, l + 1):
                if s[i - 1] == s[-j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
        return k >= (dp[-1][-1] // 2)
