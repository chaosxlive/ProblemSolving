# https://leetcode.com/problems/is-graph-bipartite/

from typing import List
from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        isAMap = {}
        for n in range(len(graph)):
            if n not in isAMap:
                isAMap[n] = True
                q = deque([n])
                while q:
                    node = q.popleft()
                    isA = isAMap[node]
                    for neighbor in graph[node]:
                        if neighbor in isAMap:
                            if isAMap[neighbor] == isA:
                                return False
                        else:
                            isAMap[neighbor] = not isA
                            q.append(neighbor)
        return True
