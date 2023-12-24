# https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/

from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(1, len(nums) - i + 1):
                ns = nums[:i] + nums[i + j:]
                isValid = True
                for k in range(1, len(ns)):
                    if ns[k] <= ns[k - 1]:
                        isValid = False
                        break
                if isValid:
                    result += 1
        return result
