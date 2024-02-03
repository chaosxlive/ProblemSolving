# https://leetcode.com/problems/type-of-triangle-ii/

from typing import List


class Solution:

    def triangleType(self, nums: List[int]) -> str:
        if nums[0] + nums[1] <= nums[2] or nums[0] + nums[2] <= nums[1] or nums[2] + nums[1] <= nums[0]:
            return 'none'
        if abs(nums[0] - nums[1]) >= nums[2] or abs(nums[0] - nums[2]) >= nums[1] or abs(nums[2] - nums[1]) >= nums[0]:
            return 'none'
        if nums[0] == nums[1] and nums[0] == nums[2]:
            return 'equilateral'
        if nums[0] == nums[1] or nums[0] == nums[2] or nums[2] == nums[1]:
            return 'isosceles'
        return 'scalene'
