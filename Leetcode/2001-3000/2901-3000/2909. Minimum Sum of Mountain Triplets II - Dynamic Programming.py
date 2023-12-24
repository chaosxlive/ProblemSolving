# https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/

from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        INF = 2147483647
        result = [INF] * len(nums)
        leftMin = nums[0]
        for i in range(1, len(nums)):
            if leftMin < nums[i]:
                result[i] = leftMin + nums[i]
            else:
                leftMin = nums[i]
        rightMin = nums[-1]
        for i in reversed(range(len(nums) - 1)):
            if rightMin < nums[i]:
                result[i] += rightMin
            else:
                result[i] = INF
                rightMin = nums[i]
        result = min(result[1:-1])
        return -1 if result >= INF else result
