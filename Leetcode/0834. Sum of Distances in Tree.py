# https://leetcode.com/problems/sum-of-distances-in-tree/

from typing import List
from collections import deque


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Setup connection between nodes
        childNodes = [[] for i in range(n)]
        for x, y in edges:
            childNodes[x].append(y)
            childNodes[y].append(x)

        # The DFS do following steps:
        # 1. Find children nodes count for each node. (Store into childrenCnts)
        # 2. Setup parent node. (Store into parent)
        # 3. Cnt root node (node 0) answer (Store into result[0]).
        childrenCnts = [0] * n
        parent = [None] * n
        result = [0] * n
        seen = set()

        def dfs(node: int, rank: int) -> None:
            result[0] += rank
            childrenCnt = 0
            for childNode in childNodes[node]:
                if childNode not in seen:
                    seen.add(childNode)
                    parent[childNode] = node
                    dfs(childNode, rank + 1)
                    childrenCnt += childrenCnts[childNode] + 1
            childrenCnts[node] = childrenCnt

        seen.add(0)
        dfs(0, 0)

        # Use BFS to solve rest nodes' answer by this formula:
        # result[i] = result[parent[i]] + n - 2 - childrenCnts[i] * 2
        q = deque(childNodes[0])
        seen.clear()
        seen.add(0)
        seen.union(childNodes[0])
        while len(q) > 0:
            node = q.popleft()
            result[node] = result[parent[node]] + n - 2 - childrenCnts[node] * 2
            for childNode in childNodes[node]:
                if childNode not in seen:
                    seen.add(childNode)
                    q.append(childNode)
        return result
