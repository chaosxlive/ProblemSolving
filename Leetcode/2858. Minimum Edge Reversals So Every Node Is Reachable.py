# https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/

from typing import List
from collections import defaultdict
from functools import lru_cache


class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        neighborUndirs = defaultdict(set)
        neighborDirs = defaultdict(set)
        for a, b in edges:
            neighborUndirs[a].add(b)
            neighborUndirs[b].add(a)
            neighborDirs[a].add(b)

        result = []

        seen = set()
        @lru_cache(None)
        def dfs(parent, child):
            seen.add(child)
            result = 0
            if child not in neighborDirs[parent]:
                result += 1
            for neighbor in neighborUndirs[child]:
                if neighbor in seen:
                    continue
                result += dfs(child, neighbor)
            return result

        for i in range(n):
            seen.clear()
            neighborDirs[None].add(i)
            result.append(dfs(None, i))
        return result
