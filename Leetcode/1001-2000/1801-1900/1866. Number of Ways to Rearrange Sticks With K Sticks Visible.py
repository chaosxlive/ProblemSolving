# https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/

class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        dp = [[0 for i in range(1001)] for j in range(1001)]
        dp[1][1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i][j] = (i - 1) * dp[i - 1][j] + dp[i - 1][j - 1]
        return dp[n][k] % 1000000007