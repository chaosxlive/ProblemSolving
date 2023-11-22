# https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

from typing import List


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return len(edges)
        self.ufAlice = {}
        self.ufBob = {}
        self.result = 0
        edges.sort(reverse=True)
        for type, x, y in edges:
            if type == 1:
                self.unionAlice(x, y)
            elif type == 2:
                self.unionBob(x, y)
            else:
                self.unionAll(x, y)
        for i in range(2, n + 1):
            if self.findAlice(1) != self.findAlice(i):
                return -1
            if self.findBob(1) != self.findBob(i):
                return -1
        return self.result

    def findAlice(self, x):
        if x not in self.ufAlice:
            self.ufAlice[x] = x
        elif self.ufAlice[x] != x:
            self.ufAlice[x] = self.findAlice(self.ufAlice[x])
        return self.ufAlice[x]

    def unionAlice(self, x, y):
        rx, ry = self.findAlice(x), self.findAlice(y)
        if rx != ry:
            self.ufAlice[rx] = ry
        else:
            self.result += 1

    def findBob(self, x):
        if x not in self.ufBob:
            self.ufBob[x] = x
        elif self.ufBob[x] != x:
            self.ufBob[x] = self.findBob(self.ufBob[x])
        return self.ufBob[x]

    def unionBob(self, x, y):
        rx, ry = self.findBob(x), self.findBob(y)
        if rx != ry:
            self.ufBob[rx] = ry
        else:
            self.result += 1

    def unionAll(self, x, y):
        rxAlice, ryAlice = self.findAlice(x), self.findAlice(y)
        rxBob, ryBob = self.findBob(x), self.findBob(y)
        if rxAlice == ryAlice and rxBob == ryBob:
            self.result += 1
            return
        if rxAlice != ryAlice:
            self.ufAlice[rxAlice] = ryAlice
        if rxBob != ryBob:
            self.ufBob[rxBob] = ryBob
