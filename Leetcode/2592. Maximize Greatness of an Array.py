# https://leetcode.com/problems/maximize-greatness-of-an-array/

from typing import List


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        result, left, right = 0, 0, 1
        while right < len(nums):
            if nums[left] > nums[right]:
                result += 1
                left += 1
            right += 1
        return result
