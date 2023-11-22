# https://leetcode.com/problems/count-nice-pairs-in-an-array/

from typing import List
from collections import defaultdict


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9+7

        def rev(n):
            return int(str(n)[::-1])

        d = defaultdict(list)
        for num in nums:
            d[num - rev(num)].append(num)

        result = 0
        for ls in d.values():
            l = len(ls)
            if l > 1:
                result += l * (l - 1) // 2
                result %= MOD
        return result
