# https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/

from collections import defaultdict
from typing import List


class Solution:

    def numberOfSubarrays(self, nums: List[int]) -> int:
        NUMS = sorted(map(lambda x: (x[1], x[0]), enumerate(nums)))

        uf = {}

        def find(x):
            if x not in uf:
                uf[x] = x
            elif uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                uf[rx] = ry

        cached = defaultdict(int)

        res = 0
        seen = [False] * len(nums)
        for n, i in NUMS:
            seen[i] = True
            r = 1
            if i > 0 and seen[i - 1]:
                if nums[find(i - 1)] == n:
                    r += cached[find(i - 1)]
                union(i - 1, i)
            if i < len(nums) - 1 and seen[i + 1]:
                if nums[find(i + 1)] == n:
                    r += cached[find(i + 1)]
                union(i + 1, i)
            cached[find(i)] = r
            res += r
        return res
