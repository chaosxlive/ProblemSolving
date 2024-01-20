from typing import List


class Solution:

    def minimumCost(self, nums: List[int]) -> int:
        result = 2147483647
        for i in range(1, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                result = min(result, nums[i] + nums[j] + nums[0])
        return result
