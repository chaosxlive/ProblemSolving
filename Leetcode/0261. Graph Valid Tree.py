# https://leetcode.com/problems/graph-valid-tree/

from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        connections = [[] for i in range(n)]
        for ea, eb in edges:
            connections[ea].append(eb)
            connections[eb].append(ea)

        seen = set()

        def dfs(parent:int, node: int) -> bool:
            for child in connections[node]:
                if child == parent:
                    continue
                if child in seen:
                    return False
                seen.add(child)
                if not dfs(node, child):
                    return False
            return True
        
        seen.add(0)
        return dfs(-1, 0) and len(seen) == n