# https://leetcode.com/problems/tuple-with-same-product/

from collections import defaultdict
from typing import List


class Solution:

    def tupleSameProduct(self, nums: List[int]) -> int:
        d = defaultdict(int)
        L = len(nums)
        result = 0
        for i in range(L - 1):
            n1 = nums[i]
            for j in range(i + 1, L):
                n2 = nums[j]
                result += d[n1 * n2]
                d[n1 * n2] += 1
        return result * 8
