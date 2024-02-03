# https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

from collections import Counter
from functools import lru_cache
from typing import List


class Solution:

    def maximumLength(self, nums: List[int]) -> int:
        counter = Counter(nums)

        @lru_cache(None)
        def solve(n):
            if n == 1:
                return counter[1] if counter[1] & 1 else counter[1] - 1
            if counter[n] == 1:
                return 1
            if n * n not in counter:
                return 1
            return 2 + solve(n * n)

        return max(solve(n) for n in nums)
