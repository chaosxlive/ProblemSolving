# https://leetcode.com/problems/house-robber/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = [0, 0]  # Take, Skip
        for num in nums:
            prev = [prev[1] + num, max(prev)]
        return max(prev)
