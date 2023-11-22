# https://leetcode.com/problems/k-inverse-pairs-array/

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0 for j in range(k + 1)] for i in range(n + 1)]
        dp[0][0] = 1
        for i in range(n):
            dp[i + 1][0] = 1
            for j in range(k):
                dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j] - (dp[i][j - i] if j >= i else 0)) % 1000000007
        return dp[n][k]
