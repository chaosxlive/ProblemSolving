# https://leetcode.com/problems/house-robber-ii/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        def calcPartialRob(nums: List[int], start: int, end: int) -> int:
            prev = [0, 0]  # Take, Skip
            for i in range(start, end):
                prev = [prev[1] + nums[i], max(prev)]
            return max(prev)

        # Case 1: Take first, so 0 is take and 1, -1 is skip
        result1 = calcPartialRob(nums, 2, len(nums) - 1) + nums[0]
        # Case 2: Skip first, so 0 is skip and treat rest as normal.
        result2 = calcPartialRob(nums, 1, len(nums))
        return max(result1, result2)
