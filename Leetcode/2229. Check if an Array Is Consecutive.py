# https://leetcode.com/problems/check-if-an-array-is-consecutive/

from typing import List


class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != nums[0] + i:
                return False
        return True
