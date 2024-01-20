# https://leetcode.com/problems/tuple-with-same-product/

from collections import defaultdict
from itertools import combinations, starmap
from operator import mul
from typing import List


class Solution:

    def tupleSameProduct(self, nums: List[int]) -> int:
        d = defaultdict(int)
        result = 0
        for p in starmap(mul, combinations(nums, 2)):
            result += d[p]
            d[p] += 1
        return result * 8
