# https://leetcode.com/problems/coin-change-ii/

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(c, len(dp)):
                dp[i] += dp[i - c]
        return dp[-1]
