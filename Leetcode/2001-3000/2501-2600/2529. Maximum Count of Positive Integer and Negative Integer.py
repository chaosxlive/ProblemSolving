# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(len(nums) - bisect_right(nums, 0), bisect_left(nums, 0))
