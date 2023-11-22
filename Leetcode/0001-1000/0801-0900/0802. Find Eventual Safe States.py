# https://leetcode.com/problems/find-eventual-safe-states/

from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        isSafe = {}

        def dfs(node: int):
            isSafe[node] = False
            result = True
            for nextNode in graph[node]:
                if nextNode not in isSafe:
                    dfs(nextNode)
                if not isSafe[nextNode]:
                    result = False
            isSafe[node] = result

        result = []
        for node in range(len(graph)):
            if node not in isSafe:
                dfs(node)
            if isSafe[node]:
                result.append(node)
        return result
