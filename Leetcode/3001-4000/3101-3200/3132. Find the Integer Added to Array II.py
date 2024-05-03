# https://leetcode.com/problems/find-the-integer-added-to-array-ii/

from math import inf
from typing import List


class Solution:

    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        L1 = len(nums1)
        L2 = len(nums2)
        nums1.sort()
        nums2.sort()
        res = inf
        for i in range(3):
            diff = nums2[0] - nums1[i]
            i1 = 0
            i2 = 0
            cnt = 0
            isValid = True
            while i2 < L2:
                while nums2[i2] - nums1[i1] != diff:
                    cnt += 1
                    if cnt > 2:
                        isValid = False
                        break
                    i1 += 1
                if not isValid:
                    break
                i2 += 1
                i1 += 1
            cnt += L1 - i1
            if isValid and cnt == 2:
                res = min(res, diff)
        return res
