# https://leetcode.com/problems/tuple-with-same-product/

from collections import Counter
from itertools import combinations, starmap
from operator import mul
from typing import List


class Solution:

    def tupleSameProduct(self, nums: List[int]) -> int:
        return sum(n * (n - 1) // 2 for n in Counter(starmap(mul, combinations(nums, 2))).values() if n > 1) * 8
