# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        result = -1
        seen = set()
        for num in nums:
            if -num in seen:
                result = max(result, abs(num))
            seen.add(num)
        return result
