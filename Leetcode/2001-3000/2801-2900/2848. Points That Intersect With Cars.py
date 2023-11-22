# https://leetcode.com/problems/points-that-intersect-with-cars/

from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        lastCover = 0
        result = 0
        for s, e in nums:
            result += max(e - max(lastCover, s - 1), 0)
            lastCover = max(e, lastCover)
        return result
