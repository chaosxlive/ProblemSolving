# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        left = 0
        idx = 1
        while idx < len(nums) and nums[left] == nums[idx]:
            idx += 1
        result = 0
        while idx < len(nums):
            right = idx + 1
            while right < len(nums) and nums[idx] == nums[right]:
                right += 1
            if right >= len(nums):
                break
            if (nums[left] > nums[idx] and nums[right] > nums[idx]) or (nums[left] < nums[idx] and nums[right] < nums[idx]):
                result += 1
            left = idx
            idx = right
        return result
