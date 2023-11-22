# https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/

from typing import List


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:

        def check(l, r):
            if nums[l] % 2 != 0:
                return 0
            for i in range(l, r):
                if nums[i] % 2 == nums[i + 1] % 2:
                    return 0
                if nums[i] > threshold:
                    return 0
            if nums[r] > threshold:
                return 0
            return r - l + 1

        result = 0
        for il in range(len(nums)):
            for ir in range(il, len(nums)):
                result = max(result, check(il, ir))
        return result
