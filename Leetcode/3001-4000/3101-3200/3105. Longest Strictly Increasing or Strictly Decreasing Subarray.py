# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

from typing import List


class Solution:

    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        decL, incL, r = 0, 0, 1
        L = len(nums)
        res = 0
        while r < L:
            if nums[r] >= nums[r - 1]:
                res = max(res, r - decL)
                decL = r
            if nums[r] <= nums[r - 1]:
                res = max(res, r - incL)
                incL = r
            r += 1
        res = max(res, r - decL)
        res = max(res, r - incL)
        return res
