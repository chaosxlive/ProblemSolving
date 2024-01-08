# https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        i = 1
        s = nums[0]
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            s += nums[i]
            i += 1
        allN = set(nums)
        while s in allN:
            s += 1
        return s
