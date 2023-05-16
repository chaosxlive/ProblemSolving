# https://leetcode.com/problems/wiggle-sort/

from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if i % 2 == 1:
                if nums[i - 1] > nums[i]:
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]
            elif i != 0 and nums[i - 1] < nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
