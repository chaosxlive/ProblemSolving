# https://leetcode.com/problems/count-pairs-in-two-arrays/

from bisect import bisect_left
from typing import List


class Solution:

    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        diffs = sorted(map(lambda x: x[0] - x[1], zip(nums1, nums2)))
        res = 0
        for i in range(1, len(diffs)):
            j = bisect_left(diffs, -diffs[i] + 1, hi=i)
            res += i - j
        return res
