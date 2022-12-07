# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        left, right = 0, len(nums)
        while left < right:
            center = left + (right - left) // 2
            if center < nums[center]:
                left = center + 1
            else:
                right = center       
        return -1 if left < len(nums) and left == nums[left] else left
