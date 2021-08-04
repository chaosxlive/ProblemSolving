# https://leetcode.com/problems/4sum-ii/

from collections import defaultdict


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        history = defaultdict(int)
        result = 0
        for a in nums1:
            for b in nums2:
                history[-(a + b)] += 1

        for c in nums3:
            for d in nums4:
                if c + d in history:
                    result += history[c + d]

        return result
