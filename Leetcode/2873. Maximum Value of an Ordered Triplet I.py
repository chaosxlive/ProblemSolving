# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = 0
        maxNum = max(nums[0], nums[1])
        maxDiff = nums[0] - nums[1]
        for i in range(2, len(nums)):
            num = nums[i]
            result = max(result, maxDiff * num)
            maxDiff = max(maxDiff, maxNum - num)
            maxNum = max(maxNum, num)
        return result
