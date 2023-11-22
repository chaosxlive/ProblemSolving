# https://leetcode.com/problems/intersection-of-three-sorted-arrays/

from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return sorted(set(arr1).intersection(arr2).intersection(arr3))
