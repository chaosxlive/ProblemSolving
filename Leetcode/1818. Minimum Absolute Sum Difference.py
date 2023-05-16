# https://leetcode.com/problems/minimum-absolute-sum-difference/

from typing import List
from bisect import bisect_left


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        candidates = sorted(nums1)
        diff = 0
        for n1, n2 in zip(nums1, nums2):
            diff = (diff + abs(n1 - n2)) % 1000000007

        result = diff
        for n1, n2 in zip(nums1, nums2):
            idx = bisect_left(candidates, n2)
            if idx - 1 >= 0:
                result = min(result, (diff - abs(n1 - n2) + abs(candidates[idx - 1] - n2)))
            if idx < len(nums1):
                result = min(result, (diff - abs(n1 - n2) + abs(candidates[idx] - n2)))
        return result % 1000000007
