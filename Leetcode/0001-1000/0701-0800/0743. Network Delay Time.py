# https://leetcode.com/problems/network-delay-time/

import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[-1 for col in range(n + 1)] for row in range(n + 1)]
        for source, target, time in times:
            graph[source][target] = time

        visited = set()
        next = []
        heapq.heappush(next, (0, k))
        arrived = [2147483647] * (n + 1)

        result = 0
        while len(next) != 0:
            time, vertex = heapq.heappop(next)
            if vertex in visited:
                continue
            visited.add(vertex)

            arrived[vertex] = time
            result = max(result, time)

            for neighbor in range(1, n + 1):
                if neighbor == vertex or neighbor in visited:
                    continue

                if graph[vertex][neighbor] != -1 and time + graph[vertex][neighbor] < arrived[neighbor]:
                    heapq.heappush(next, (time + graph[vertex][neighbor], neighbor))

        return result if len(visited) == n else -1
