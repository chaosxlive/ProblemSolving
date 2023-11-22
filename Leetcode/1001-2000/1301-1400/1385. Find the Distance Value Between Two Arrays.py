# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        result = len(arr1)
        for x in arr1:
            for y in arr2:
                if abs(x - y) <= d:
                    result -= 1
                    break
        return result
