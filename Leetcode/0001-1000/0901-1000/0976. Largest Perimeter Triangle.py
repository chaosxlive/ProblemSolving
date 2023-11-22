# https://leetcode.com/problems/largest-perimeter-triangle/

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2] and nums[i + 2] > nums[i] - nums[i + 1]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0
