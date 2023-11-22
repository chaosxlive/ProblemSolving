# https://leetcode.com/problems/longest-alternating-subarray/

from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        result = 0
        for l in range(len(nums) - 1):
            for r in range(l + 1, len(nums)):
                m = 1
                isValid = True
                for i in range(l, r):
                    if nums[i] + m != nums[i + 1]:
                        isValid = False
                        break
                    m *= -1
                if isValid:
                    result = max(result, r - l + 1)
        return result if result > 0 else -1
