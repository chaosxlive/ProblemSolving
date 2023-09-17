# https://leetcode.com/problems/maximum-number-of-pairs-in-array/

from typing import List
from collections import Counter


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        result = [0, 0]
        for c in Counter(nums).values():
            result[0] += c // 2
            result[1] += c % 2
        return result
