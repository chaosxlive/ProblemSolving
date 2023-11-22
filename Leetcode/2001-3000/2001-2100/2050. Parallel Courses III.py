# https://leetcode.com/problems/parallel-courses-iii/

from typing import List
from functools import lru_cache


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        children = [[] for _ in range(n + 1)]
        isRoot = [True] * (n + 1)
        for a, b in relations:
            children[b].append(a)
            isRoot[a] = False

        @lru_cache(None)
        def dfs(node):
            res = 0
            for child in children[node]:
                res = max(res, dfs(child))
            return res + time[node - 1]

        result = 0
        for i in range(1, n + 1):
            if isRoot[i]:
                result = max(result, dfs(i))
        return result
