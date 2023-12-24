# https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/

from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        result = 2147483647
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        result = min(result, nums[i] + nums[j] + nums[k])
        return -1 if result == 2147483647 else result
