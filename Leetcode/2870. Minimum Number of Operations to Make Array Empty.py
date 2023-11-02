# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

from typing import List
from collections import Counter


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        result = 0
        for v in c.values():
            if v == 1:
                return -1
            r = v % 6
            if r == 0 or r == 3:
                result += v // 3
            else:
                result += (v // 3) + 1
        return result
