# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

from typing import List
from itertools import accumulate


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        prefixSum = list(accumulate(arr))
        target = prefixSum[-1] // 3
        if target != prefixSum[-1] / 3:
            return False
        idx = 0
        while idx < len(arr) - 2 and prefixSum[idx] != target:
            idx += 1
        if idx == len(arr) - 2:
            return False
        target *= 2
        idx += 1
        while idx < len(arr) - 1 and prefixSum[idx] != target:
            idx += 1
        return idx != len(arr) - 1
