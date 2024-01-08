# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

from functools import reduce
from operator import xor
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        allXor = reduce(xor, nums)
        allXor ^= k
        result = 0
        while allXor > 0:
            result += allXor & 1
            allXor >>= 1
        return result
