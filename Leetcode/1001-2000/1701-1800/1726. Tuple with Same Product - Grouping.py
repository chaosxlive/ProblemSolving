# https://leetcode.com/problems/tuple-with-same-product/

from collections import defaultdict
from typing import List


class Solution:

    def tupleSameProduct(self, nums: List[int]) -> int:
        d = defaultdict(list)
        L = len(nums)
        for i in range(L - 1):
            n1 = nums[i]
            for j in range(i + 1, L):
                n2 = nums[j]
                d[n1 * n2].append((n1, n2))
        result = 0
        for l in d.values():
            ll = len(l)
            if ll > 1:
                result += ll * (ll - 1) // 2
        return result * 8
