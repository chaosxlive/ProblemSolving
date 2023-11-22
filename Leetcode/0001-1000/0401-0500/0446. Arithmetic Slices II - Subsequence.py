# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total = 0
        dp = [defaultdict(lambda: 0) for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                dp[i][nums[i] - nums[j]] += 1
                if nums[i] - nums[j] in dp[j]:
                    dp[i][nums[i] - nums[j]] += dp[j][nums[i] - nums[j]]
                    total += dp[j][nums[i] - nums[j]]
        return total
