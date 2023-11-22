# https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/

from typing import List
from functools import reduce


class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        final = reduce(lambda a, b: a & b, nums, 2147483647)
        if final != 0:
            return 1
        result = 0
        curr = 2147483647
        for num in nums:
            curr &= num
            if curr == final:
                result += 1
                curr = 2147483647
        return result
