# https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/

from typing import List


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] % 2 == 0 and nums[j] % 2 == 0:
                    return True
        return False
