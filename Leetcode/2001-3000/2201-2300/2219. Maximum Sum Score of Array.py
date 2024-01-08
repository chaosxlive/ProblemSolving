# https://leetcode.com/problems/maximum-sum-score-of-array/

from itertools import accumulate
from typing import List


class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        prefix = [0] + list(accumulate(nums))
        return max(max(prefix[i + 1], prefix[-1] - prefix[i]) for i in range(len(nums)))
