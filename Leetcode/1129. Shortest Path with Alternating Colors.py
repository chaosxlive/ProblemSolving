# https://leetcode.com/problems/shortest-path-with-alternating-colors/

from typing import List
from collections import deque, defaultdict


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        result = [-1 for i in range(n)]
        redWalked = set()
        blueWalked = set()
        nextPath = defaultdict(lambda: [[], []])  # Red, Blue
        for start, end in redEdges:
            nextPath[start][0].append(end)
        for start, end in blueEdges:
            nextPath[start][1].append(end)

        q = deque([(0, True, 0), (0, False, 0)])
        while q:
            nodeId, isRed, step = q.popleft()
            if result[nodeId] == -1:
                result[nodeId] = step
            if isRed:
                for nextNode in nextPath[nodeId][1]:
                    if nextNode not in blueWalked:
                        blueWalked.add(nextNode)
                        q.append((nextNode, False, step + 1))
            else:
                for nextNode in nextPath[nodeId][0]:
                    if nextNode not in redWalked:
                        redWalked.add(nextNode)
                        q.append((nextNode, True, step + 1))
        return result
