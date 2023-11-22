# https://leetcode.com/problems/find-if-path-exists-in-graph/

from queue import Queue


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        paths = {i: [] for i in range(n)}
        for u, v in edges:
            paths[u].append(v)
            paths[v].append(u)

        visited = set()
        queue = Queue()
        queue.put(source)
        while not queue.empty():
            node = queue.get()
            if node == destination:
                return True
            if node in visited:
                continue
            visited.add(node)
            for next_node in paths[node]:
                queue.put(next_node)
        return False
