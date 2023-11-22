# https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

from typing import List


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.dp = [[2147483647] * n for _ in range(n)]
        for a, b, cost in edges:
            self.dp[a][b] = cost
        for i in range(n):
            self.dp[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    self.dp[i][j] = min(self.dp[i][j], self.dp[i][k] + self.dp[k][j])

    def addEdge(self, edge: List[int]) -> None:
        a, b, cost = edge
        for i in range(self.n):
            for j in range(self.n):
                self.dp[i][j] = min(self.dp[i][j],
                                    self.dp[i][a] + cost + self.dp[b][j])

    def shortestPath(self, node1: int, node2: int) -> int:
        return -1 if self.dp[node1][node2] == 2147483647 else self.dp[node1][node2]


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
