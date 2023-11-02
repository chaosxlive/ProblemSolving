# https://leetcode.com/problems/maximum-number-of-k-divisible-components/

from typing import List


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        neighbors = [[] for _ in range(n)]
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)

        seen = [False] * n
        self.result = 1

        def dfs(node, s):
            seen[node] = True
            for neighbor in neighbors[node]:
                if not seen[neighbor]:
                    ns = dfs(neighbor, 0)
                    if ns % k == 0:
                        self.result += 1
                    else:
                        s += ns
            return s + values[node]

        dfs(0, 0)
        return self.result
