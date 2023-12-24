# https://leetcode.com/problems/minimize-product-sum-of-two-arrays/

from itertools import starmap
from operator import mul
from typing import List


class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        return sum(starmap(mul, zip(sorted(nums1), sorted(nums2, reverse=True))))
