# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

from typing import List
from itertools import accumulate


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefixSum = [0] + list(accumulate(nums))
        lastSeen = {}
        for i, n in enumerate(prefixSum):
            lastSeen[n] = i
        result = 0
        for prefixIdx in range(len(nums)):
            if prefixSum[prefixIdx] + k in lastSeen:
                result = max(result, lastSeen[prefixSum[prefixIdx] + k] - prefixIdx)
        return result
