from math import inf
from typing import List, Optional


class Solution:

    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        L1 = len(nums1)
        L2 = len(nums2)
        nums1.sort()
        nums2.sort()
        res = inf
        for a in range(L1 - 1):
            for b in range(a + 1, L1):
                newNums1 = [0] * (L1 - 2)
                i = 0
                j = 0
                while i < L1:
                    if i == a or i == b:
                        i += 1
                        continue
                    newNums1[j] = nums1[i]
                    i += 1
                    j += 1
                isValid = True
                for i in range(1, L2):
                    if nums2[i] - newNums1[i] != nums2[0] - newNums1[0]:
                        isValid = False
                        break
                if isValid:
                    res = min(res, nums2[0] - newNums1[0])
        return res
