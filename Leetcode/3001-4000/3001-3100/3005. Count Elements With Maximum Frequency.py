# https://leetcode.com/problems/count-elements-with-maximum-frequency/

from collections import Counter
from typing import List


class Solution:

    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        f = max(c.values())
        result = 0
        for v in c.values():
            if v == f:
                result += v

        return result
