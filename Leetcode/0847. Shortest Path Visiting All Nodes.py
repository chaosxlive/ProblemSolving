# https://leetcode.com/problems/shortest-path-visiting-all-nodes/

from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        dp = [[2147483647] * (len(graph) + 1) for i in range(2 ** (len(graph) + 1))]
        seen = set()

        def dfs(mask: int, node: int) -> int:
            if (mask, node) in seen:
                return dp[mask][node]
            if mask == (1 << len(graph)) - 1:
                return 0
            seen.add((mask, node))
            for nextNode in graph[node]:
                dp[mask][node] = min(
                    dp[mask][node],
                    dfs(mask, nextNode) + 1,
                    dfs(mask | 1 << nextNode, nextNode) + 1,
                )
            return dp[mask][node]

        result = 2147483647
        for node in range(len(graph)):
            result = min(result, dfs(1 << node, node))
        return result
