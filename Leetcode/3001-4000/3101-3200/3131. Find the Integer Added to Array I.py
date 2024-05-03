# https://leetcode.com/problems/find-the-integer-added-to-array-i/

from typing import List


class Solution:

    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return min(nums2) - min(nums1)
