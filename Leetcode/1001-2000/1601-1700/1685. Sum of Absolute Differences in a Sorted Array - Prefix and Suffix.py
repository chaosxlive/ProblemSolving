# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prev = [0] * l
        post = [0] * l
        for i in range(1, l):
            prev[i] = prev[i - 1] + nums[i - 1]
        for i in reversed(range(l - 1)):
            post[i] = post[i + 1] + nums[i + 1]
        result = [0] * l
        for i, n in enumerate(nums):
            result[i] = (2 * i - l + 1) * n + post[i] - prev[i]
        return result
