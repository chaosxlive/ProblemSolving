# https://leetcode.com/problems/longest-cycle-in-a-graph/

from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = [[-1, -1]] * len(edges)
        self.result = -1

        def dfs(startId, node, step):
            if visited[node][1] != -1:
                if visited[node][0] != startId:
                    return
                self.result = max(self.result, step - visited[node][1])
                return
            else:
                visited[node] = [startId, step]
            if edges[node] != -1:
                dfs(startId, edges[node], step + 1)

        for n in range(len(edges)):
            if visited[n][1] == -1:
                dfs(n, n, 0)
        return self.result
