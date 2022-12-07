# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        result = []
        total = sum(nums)
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            result.append(nums[i])
            if s > total - s:
                return result
        return []
