# https://leetcode.com/problems/stone-game-vii/

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        stoneSum = [0] * (len(stones) + 1)
        for i in range(len(stones)):
            stoneSum[i + 1] = stoneSum[i] + stones[i]
        dp = [[0 for j in range(len(stones))] for i in range(len(stones))]
        for length in range(2, len(stones) + 1):
            left = 0
            while left + length - 1 < len(stones):
                right = left + length - 1
                dp[left][right] = max(stoneSum[right + 1] - stoneSum[left + 1] - dp[left + 1][right], stoneSum[right] - stoneSum[left] - dp[left][right - 1])
                left += 1
        return dp[0][len(stones) - 1]
