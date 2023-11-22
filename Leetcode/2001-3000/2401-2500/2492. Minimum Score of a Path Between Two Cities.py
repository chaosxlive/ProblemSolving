# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
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

        for road in roads:
            union(road[0], road[1])

        target = find(n)
        return min([v for [s, e, v] in roads if find(s) == target and find(e) == target])
