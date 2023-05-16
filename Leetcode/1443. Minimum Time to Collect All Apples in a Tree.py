# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

from typing import List
from collections import defaultdict


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.hasApple = hasApple
        self.nextNodes = defaultdict(list)
        for x, y in edges:
            self.nextNodes[x].append(y)
            self.nextNodes[y].append(x)

        self.seen = set()
        self.result = 0

        self.dfs(0, 0, 0)

        return self.result * 2

    def dfs(self, node, rank, walkedRank):
        self.seen.add(node)
        result = False
        if self.hasApple[node]:
            self.result += rank - walkedRank
            walkedRank = rank
            result = True
        for n in self.nextNodes[node]:
            if n not in self.seen and self.dfs(n, rank + 1, walkedRank):
                walkedRank = rank
                result = True
        return result
