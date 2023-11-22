# https://leetcode.com/problems/smallest-string-with-swaps/

from typing import List
from collections import defaultdict, deque


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
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

        for x, y in pairs:
            union(x, y)

        swapable = defaultdict(deque)
        for c, i in sorted(map(lambda x: (x[1], x[0]), enumerate(s))):
            swapable[find(i)].append(c)

        result = []
        for i in range(len(s)):
            result.append(swapable[find(i)].popleft())
        return ''.join(result)
