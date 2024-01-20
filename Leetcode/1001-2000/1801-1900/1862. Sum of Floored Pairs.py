# https://leetcode.com/problems/sum-of-floored-pairs/

from collections import Counter
from itertools import accumulate
from typing import List


class Solution:

    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        M = max(nums)
        c = Counter(nums)
        lookups = [0] * (M + 1)
        for n, v in c.items():
            for i in range(n, M + 1, n):
                lookups[i] += v
        acc = list(accumulate(lookups))
        return sum(acc[n] * v for n, v in c.items()) % (10**9 + 7)
