# https://leetcode.com/problems/find-common-elements-between-two-arrays/

from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [0, 0]
        s1 = set(nums1)
        s2 = set(nums2)
        for n in nums1:
            if n in s2:
                result[0] += 1
        for n in nums2:
            if n in s1:
                result[1] += 1
        return result
