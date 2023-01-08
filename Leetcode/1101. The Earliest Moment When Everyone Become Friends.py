# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

from typing import List


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        self.uf = {}
        self.lastUpdate = -1
        logs.sort()
        for t, x, y in logs:
            self.union(x, y, t)
        for i in range(1, n):
            if self.find(i) != self.find(0):
                return -1
        return self.lastUpdate

    def find(self, x):
        if x not in self.uf:
            self.uf[x] = x
        elif self.uf[x] != x:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def union(self, x, y, t):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.lastUpdate = t
            self.uf[rx] = ry
