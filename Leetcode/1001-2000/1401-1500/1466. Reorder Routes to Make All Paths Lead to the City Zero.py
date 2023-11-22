# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

from typing import List
from collections import defaultdict, deque


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        path = defaultdict(list)  # nextNode, isStart
        for start, end in connections:
            path[start].append((end, True))
            path[end].append((start, False))

        result = 0
        seen = set([0])
        q = deque([0])
        while q:
            node = q.popleft()
            for nextNode, isStart in path[node]:
                if nextNode not in seen:
                    seen.add(nextNode)
                    if isStart:
                        result += 1
                    q.append(nextNode)
        return result
