# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0
        left, right = 0, len(nums) - 1
        while left <= right:
            center = left + (right - left) // 2
            if nums[center] < target:
                if nums[center] < nums[0] and nums[0] < target:
                    right = center - 1
                else:
                    left = center + 1
            elif nums[center] > target:
                if nums[center] >= nums[0] and nums[0] > target:
                    left = center + 1
                else:
                    right = center - 1
            else:
                return center
        return -1
