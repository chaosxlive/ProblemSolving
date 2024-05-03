# https://leetcode.com/problems/minimum-height-trees/

from typing import List


class Solution:

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        adjs = [set() for _ in range(n)]
        for a, b in edges:
            adjs[a].add(b)
            adjs[b].add(a)
        q = []
        for i, adj in enumerate(adjs):
            if len(adj) == 1:
                q.append(i)
        cnt = n
        while cnt > 2:
            nq = []
            while q:
                i = q.pop()
                cnt -= 1
                for j in adjs[i]:
                    adjs[j].discard(i)
                    if len(adjs[j]) == 1:
                        nq.append(j)
            q = nq
        return list(q)
