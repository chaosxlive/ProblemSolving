# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/

from functools import reduce
from math import inf
from operator import or_
from typing import List


class Solution:

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res = inf
        for l in range(1, len(nums) + 1):
            for i in range(len(nums) - l + 1):
                s = reduce(or_, nums[i:i + l])
                if s >= k:
                    res = min(res, l)
        return -1 if res == inf else res
