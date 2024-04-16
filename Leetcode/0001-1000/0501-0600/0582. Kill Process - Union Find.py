# https://leetcode.com/problems/kill-process/

from typing import List


class Solution:

    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
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

        for p, pp in zip(pid, ppid):
            if p == kill:
                continue
            union(p, pp)

        return [p for p in pid if find(kill) == find(p)]
