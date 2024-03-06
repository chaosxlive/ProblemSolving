# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/

from functools import lru_cache
from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:

        @lru_cache(None)
        def solve(left, right, target):
            if left >= right:
                return 0
            result = 0
            if nums[left] + nums[left + 1] == target:
                result = max(result, solve(left + 2, right, target) + 1)
            if nums[left] + nums[right] == target:
                result = max(result, solve(left + 1, right - 1, target) + 1)
            if nums[right - 1] + nums[right] == target:
                result = max(result, solve(left, right - 2, target) + 1)
            return result

        return max(
            solve(2, len(nums) - 1, nums[0] + nums[1]),
            solve(1, len(nums) - 2, nums[0] + nums[-1]),
            solve(0, len(nums) - 3, nums[-2] + nums[-1]),
        ) + 1
