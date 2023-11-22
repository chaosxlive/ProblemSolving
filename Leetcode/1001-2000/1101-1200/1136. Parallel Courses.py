# https://leetcode.com/problems/parallel-courses/

from typing import List
from collections import defaultdict
from functools import lru_cache


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        nexts = defaultdict(set)
        noPrev = set(range(1, n + 1))
        for s, e in relations:
            nexts[s].add(e)
            if e in noPrev:
                noPrev.remove(e)

        if len(noPrev) == 0:
            return -1

        seen = set()

        @lru_cache(None)
        def dfs(node):
            seen.add(node)
            result = 0
            for n in nexts[node]:
                if n in seen:
                    return -1
                ns = dfs(n)
                if ns == -1:
                    return -1
                result = max(result, ns)
            seen.remove(node)
            return result + 1

        result = 0
        for n in noPrev:
            seen.clear()
            curr = dfs(n)
            if curr == -1:
                return -1
            result = max(result, curr)
        return result
