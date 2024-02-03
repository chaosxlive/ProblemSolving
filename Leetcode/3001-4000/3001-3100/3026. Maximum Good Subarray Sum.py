# https://leetcode.com/problems/maximum-good-subarray-sum/

from collections import defaultdict
from itertools import accumulate
from typing import List


class Solution:

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0, *accumulate(nums)]
        idxMap = defaultdict(lambda: -1)
        result = -2**63
        for i, v in enumerate(nums):
            if idxMap[v] != -1:
                if prefix[i] < prefix[idxMap[v]]:
                    idxMap[v] = i
            else:
                idxMap[v] = i
            if idxMap[v - k] != -1:
                result = max(result, prefix[i + 1] - prefix[idxMap[v - k]])
            if idxMap[v + k] != -1:
                result = max(result, prefix[i + 1] - prefix[idxMap[v + k]])
        return result if result != -2**63 else 0
