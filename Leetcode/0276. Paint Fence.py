# https://leetcode.com/problems/paint-fence/

class Solution:
    def numWays(self, n: int, k: int) -> int:
        if k == 1 and n >= 3:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k * k
        dp = [k, k * (k - 1)]  # Prev 2 same color, prev 2 not same color
        for i in range(n - 2):
            dp = [dp[1], (dp[0] + dp[1]) * (k - 1)]
        return sum(dp)
