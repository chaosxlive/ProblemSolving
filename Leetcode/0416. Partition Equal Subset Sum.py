# https://leetcode.com/problems/partition-equal-subset-sum/

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        dp = [0] * (total // 2 + 1)
        for num in nums:
            for i in range(len(dp) - 1, num - 1, -1):
                dp[i] = max(dp[i], dp[i - num] + num)
        return dp[-1] == (total // 2)
