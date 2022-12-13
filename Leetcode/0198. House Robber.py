# https://leetcode.com/problems/house-robber/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0, 0]  # prevNotAndCurrentPick, prevPickAndCurrentNot, bothNotPick
        for num in nums:
            dp = [max(dp[1], dp[2]) + num, dp[0], max(dp[1], dp[2])]
        return max(dp)
