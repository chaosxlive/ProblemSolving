# https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

from typing import List
from sortedcontainers import SortedList


class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        candidates = SortedList()
        result = 2147483647
        for i in range(x, len(nums)):
            candidates.add(nums[i - x])
            j = candidates.bisect_left(nums[i])
            if j > 0:
                result = min(result, abs(nums[i] - candidates[j - 1]))
            if 0 <= j < len(candidates):
                result = min(result, abs(nums[i] - candidates[j]))
        return result
