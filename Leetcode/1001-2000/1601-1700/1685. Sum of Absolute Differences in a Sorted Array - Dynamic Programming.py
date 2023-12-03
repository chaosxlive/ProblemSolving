# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        l = len(nums)
        m = sum(nums)
        result = [0] * l
        for i, num in enumerate(nums):
            result[i] = (2 * i - l) * num + m
            m -= 2 * num
        return result