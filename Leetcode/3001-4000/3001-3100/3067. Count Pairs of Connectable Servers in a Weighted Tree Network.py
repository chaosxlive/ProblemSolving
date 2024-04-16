# https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/

from collections import defaultdict
from typing import List


class Solution:

    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        N = len(edges) + 1
        neighbors = defaultdict(list)
        for a, b, w in edges:
            neighbors[a].append((b, w))
            neighbors[b].append((a, w))

        def dfs(n, p, s):
            cnt = 0
            for neighbor, w in neighbors[n]:
                if neighbor == p:
                    continue
                cnt += dfs(neighbor, n, s + w)
            if s % signalSpeed == 0:
                cnt += 1
            return cnt

        result = [0] * N
        for i in range(N):
            if len(neighbors[i]) == 1:
                continue
            res = 0
            ss = 0
            for neighbor, w in neighbors[i]:
                r = dfs(neighbor, i, w)
                if r > 0:
                    res += ss * r
                    ss += r
            result[i] = res
        return result
