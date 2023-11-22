# https://leetcode.com/problems/count-valid-paths-in-a-tree/

from typing import List


class Solution:

    def __init__(self) -> None:
        n = 100001
        self.primes = [True] * (n + 1)
        for i in range(2, int(n ** 0.5) + 1):
            if self.primes[i]:
                for j in range(i * i, n + 1, i):
                    self.primes[j] = False
        self.primes[1] = False

    def countPaths(self, n: int, edges: List[List[int]]) -> int:

        neighbors = [[] for i in range(n + 1)]
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)

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

        for a in range(1, n + 1):
            if not self.primes[a]:
                for b in neighbors[a]:
                    if not self.primes[b]:
                        union(a, b)

        group = [[] for i in range(n + 1)]
        groupNeighborPrimes = [[] for i in range(n + 1)]

        for i in range(1, n + 1):
            if not self.primes[i]:
                group[find(i)].append(i)
            else:
                for j in neighbors[i]:
                    if not self.primes[j]:
                        groupNeighborPrimes[find(j)].append(i)
        result = 0

        cnts = [0] * (n + 1)
        for i in range(1, n + 1):
            if len(group[i]) > 0:
                for neighbor in groupNeighborPrimes[i]:
                    result += (cnts[neighbor] * len(group[i])) + len(group[i])
                    cnts[neighbor] += len(group[i])
        
        return result
