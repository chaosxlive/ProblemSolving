# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

from typing import List
from collections import defaultdict


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
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

        for x, y in edges:
            union(x, y)

        groups = defaultdict(int)
        for i in range(n):
            groups[find(i)] += 1

        result = 0
        vs = list(groups.values())
        cnt = vs[0]
        for v in vs[1:]:
            result += cnt * v
            cnt += v
        return result
