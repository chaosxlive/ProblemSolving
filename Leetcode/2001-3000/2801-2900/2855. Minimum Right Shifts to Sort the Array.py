# https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/

from typing import List


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        cutIdx = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if cutIdx != -1:
                    return -1
                cutIdx = i + 1
        if cutIdx == -1:
            return 0
        if nums[0] < nums[-1]:
            return -1
        return len(nums) - cutIdx
