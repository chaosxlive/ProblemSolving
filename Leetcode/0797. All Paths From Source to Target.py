# https://leetcode.com/problems/all-paths-from-source-to-target/

from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.pathReachTarget = {len(graph) - 1: [[]]}
        return self.dfs(0)

    def dfs(self, currentNodeIdx: int):
        if currentNodeIdx in self.pathReachTarget:
            if self.pathReachTarget[currentNodeIdx] is None:
                return None
        else:
            self.pathReachTarget[currentNodeIdx] = []
            for nextNodeIdx in self.graph[currentNodeIdx]:
                result = self.dfs(nextNodeIdx)
                if result is not None:
                    self.pathReachTarget[currentNodeIdx].extend(result)
            if len(self.pathReachTarget[currentNodeIdx]) == 0:
                self.pathReachTarget[currentNodeIdx] = None
                return None
        return list(map(lambda x: [currentNodeIdx] + x, self.pathReachTarget[currentNodeIdx]))
