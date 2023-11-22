# https://leetcode.com/problems/happy-students/

from typing import List


class Solution:
    def countWays(self, nums: List[int]) -> int:
        result = 0
        nums.sort()

        for selectedCnt in range(1, len(nums)):
            if nums[selectedCnt - 1] < selectedCnt and nums[selectedCnt] > selectedCnt:
                result += 1
        if nums[0] > 0:
            result += 1
        if nums[-1] < len(nums):
            result += 1
        return result
