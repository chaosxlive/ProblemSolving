# https://leetcode.com/problems/maximum-size-of-a-set-after-removals/

from collections import defaultdict
from typing import List


class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        ov1 = ov2 = 0
        L1 = len(nums1)
        L2 = len(nums2)
        c1 = defaultdict(int)
        c2 = defaultdict(int)
        for n in nums1:
            c1[n] += 1
            if c1[n] > 1:
                ov1 += 1
        for n in nums2:
            c2[n] += 1
            if c2[n] > 1:
                ov2 += 1
        dif1 = L1 - ov1
        dif2 = L2 - ov2
        if ov1 >= L1 // 2 and ov2 >= L2 // 2:
            return len(set(nums1).union(nums2))
        if ov1 >= L1 // 2:
            return min(len(set(nums2).difference(set(nums1))), L2 // 2) + dif1
        if ov2 >= L2 // 2:
            return min(len(set(nums1).difference(set(nums2))), L1 // 2) + dif2
        return min(len(set(nums1).union(set(nums2))), L1)
