# https://leetcode.com/problems/connecting-cities-with-minimum-cost/

from typing import List
import heapq


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        cs = list(map(lambda x: (x[2], x[0], x[1]), connections))
        heapq.heapify(cs)

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

        result = 0
        while len(cs):
            v, a, b = heapq.heappop(cs)
            if find(a) == find(b):
                continue
            result += v
            union(a, b)

        return result if len(set(map(find, range(1, n+1)))) == 1 else -1
