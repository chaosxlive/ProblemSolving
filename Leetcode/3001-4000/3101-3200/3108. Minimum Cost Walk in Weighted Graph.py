# https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

from typing import List


class Solution:

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        ands = [-1] * n
        uf = [-1] * n

        def find(x):
            if uf[x] == -1:
                uf[x] = x
            elif uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                uf[rx] = ry

        for a, b, w in edges:
            union(a, b)
            ands[a] = w if ands[a] == -1 else ands[a] & w
            ands[b] = w if ands[b] == -1 else ands[b] & w

        for i in range(n):
            t = find(i)
            ands[t] = ands[i] = ands[t] & ands[i]

        res = []

        for a, b in query:
            if find(a) != find(b):
                res.append(-1)
            elif a == b:
                res.append(0)
            else:
                res.append(ands[find(a)])

        return res
