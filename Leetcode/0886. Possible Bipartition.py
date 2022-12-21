# https://leetcode.com/problems/possible-bipartition/

from typing import List
from collections import defaultdict, deque


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
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

        hostiles = defaultdict(set)
        for x, y in dislikes:
            union(x, y)
            hostiles[x].add(y)
            hostiles[y].add(x)

        groups = set([find(x) for x in range(1, n + 1)])

        def findLoopHostile(root: int) -> bool:
            isGroupA = {root: True}
            q = deque([root])
            while len(q) > 0:
                x = q.popleft()
                for hostile in hostiles[x]:
                    if hostile in isGroupA:
                        if isGroupA[hostile] == isGroupA[x]:
                            return True
                    else:
                        isGroupA[hostile] = not isGroupA[x]
                        q.append(hostile)
            return False

        for root in groups:
            if findLoopHostile(root):
                return False
        return True
