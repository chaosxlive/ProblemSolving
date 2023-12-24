# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total = sum(nums[:2])
        result = -1
        for i in range(2, len(nums)):
            num = nums[i]
            total += num
            if num < total - num:
                result = max(result, total)
        return result
