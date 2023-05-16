# https://leetcode.com/problems/smallest-range-ii/

from typing import List


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        if k == 0:
            return nums[-1] - nums[0]
        result = nums[-1] - nums[0]
        for i in range(1, len(nums)):
            result = min(result, max(nums[i - 1] + k, nums[-1] - k) - min(nums[0] + k, nums[i] - k))
        return result
