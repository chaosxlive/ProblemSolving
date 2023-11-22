# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result = 0
        minIdx = -1
        maxIdx = -1
        left = -1
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                left = i
            if num == minK:
                minIdx = i
            if num == maxK:
                maxIdx = i
            result += max(0, min(minIdx, maxIdx) - left)
        return result
