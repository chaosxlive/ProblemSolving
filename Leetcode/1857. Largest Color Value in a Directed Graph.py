# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

from typing import List
from collections import deque


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        N = len(colors)
        neighbors = [[] for _ in range(N)]
        comes = [0] * N
        for ns, ne in edges:
            neighbors[ns].append(ne)
            comes[ne] += 1
        cnts = [[0] * 26 for _ in range(N)]
        q = deque(map(lambda x: x[0], filter(lambda x: x[1] == 0, enumerate(comes))))
        result = 0
        seenCnt = 0
        while q:
            n = q.popleft()
            cnts[n][ord(colors[n]) - 97] += 1
            result = max(result, cnts[n][ord(colors[n]) - 97])
            seenCnt += 1

            for neighbor in neighbors[n]:
                for i in range(26):
                    cnts[neighbor][i] = max(cnts[neighbor][i], cnts[n][i])
                comes[neighbor] -= 1
                if comes[neighbor] == 0:
                    q.append(neighbor)

        return result if seenCnt == N else -1
