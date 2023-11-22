# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        self.edges = edges
        result = -1
        minDist = 2147483647
        dist1 = [0] * len(edges)
        dist2 = [0] * len(edges)
        seen1 = [False] * len(edges)
        seen2 = [False] * len(edges)
        self.dfs(node1, dist1, seen1)
        self.dfs(node2, dist2, seen2)
        for node in range(len(edges)):
            if seen1[node] and seen2[node] and minDist > max(dist1[node], dist2[node]):
                minDist = max(dist1[node], dist2[node])
                result = node
        return result

    def dfs(self, node, dist, seen):
        seen[node] = True
        neighbor = self.edges[node]
        if neighbor != -1 and not seen[neighbor]:
            dist[neighbor] = dist[node] + 1
            self.dfs(neighbor, dist, seen)
