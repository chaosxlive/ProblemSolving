# https://leetcode.com/problems/number-of-good-paths/

from typing import List
from collections import defaultdict


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        neighbors = defaultdict(list)
        for x, y in edges:
            neighbors[x].append(y)
            neighbors[y].append(x)

        nodes = defaultdict(list)
        for i, v in enumerate(vals):
            nodes[v].append(i)

        nums = sorted(nodes.keys())
        
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
        for num in nums:
            for node in nodes[num]:
                for neighbor in neighbors[node]:
                    if vals[neighbor] <= vals[node]:
                        union(neighbor, node)
            group = defaultdict(int)
            for node in nodes[num]:
                group[find(node)] += 1
            for v in group.values():
                if v > 1:
                    result += v * (v - 1) // 2
                result += v
        return result
