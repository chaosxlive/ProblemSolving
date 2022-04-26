# https://leetcode.com/problems/shortest-path-visiting-all-nodes/

from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        queue = deque()

        for i in range(len(graph)):
            queue.append((i, (i,)))

        visited = set(queue)
        steps = 0

        while queue:
            newQueue = deque()
            while queue:
                node, path = queue.popleft()
                for neighbor in graph[node]:
                    newPath = path + (neighbor,)

                    if len(newPath) == len(graph):
                        return steps + 1

                    if (neighbor, newPath) not in visited:
                        newQueue.append((neighbor, newPath))
                        visited.add((neighbor, newPath))
            steps += 1
            queue = newQueue

        return steps
