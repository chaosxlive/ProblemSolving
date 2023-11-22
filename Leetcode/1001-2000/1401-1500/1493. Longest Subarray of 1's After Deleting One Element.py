# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        nums = nums + [0, 0]
        i = nums.index(0)
        if i == len(nums) - 2:
            return len(nums) - 3
        prev = i
        result = 0
        while i < len(nums) - 1:
            j = i + 1
            if nums[i] == 0:
                j = i + 1
                c = 0
                while j < len(nums) - 2 and nums[j] == 1:
                    c += 1
                    j += 1
                result = max(result, prev + c)
                prev = c
            i = j
        return result
