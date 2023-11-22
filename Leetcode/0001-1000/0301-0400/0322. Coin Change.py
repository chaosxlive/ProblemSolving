# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        for i in range(1, amount + 1):
            dp[i] = min([2147483647] + [dp[i - coin] for coin in coins if i - coin >= 0 and dp[i - coin] != -1])
            dp[i] = -1 if dp[i] == 2147483647 else dp[i] + 1
            
        return dp[amount]
