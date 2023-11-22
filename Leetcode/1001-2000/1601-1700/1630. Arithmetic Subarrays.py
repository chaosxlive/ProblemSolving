# https://leetcode.com/problems/arithmetic-subarrays/

from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        def check(nums):
            nums.sort()
            diff = nums[1] - nums[0]
            for i in range(2, len(nums)):
                if nums[i] - nums[i - 1] != diff:
                    return False
            return True

        return [check(nums[il:ir + 1]) for il, ir in zip(l, r)]
