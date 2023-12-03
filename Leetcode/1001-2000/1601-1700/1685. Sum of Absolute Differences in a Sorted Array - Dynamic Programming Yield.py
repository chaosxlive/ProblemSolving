# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        l = len(nums)
        m = sum(nums)
        for i, num in enumerate(nums):
            yield (2 * i - l) * num + m
            m -= 2 * num
