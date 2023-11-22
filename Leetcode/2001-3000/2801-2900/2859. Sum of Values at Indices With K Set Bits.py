# https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def countBit(n):
            result = 0
            while n > 0:
                result += n & 1
                n >>= 1
            return result

        result = 0
        for i in range(len(nums)):
            if countBit(i) == k:
                result += nums[i]
        return result
