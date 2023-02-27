# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

from typing import List
from collections import defaultdict


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        children = defaultdict(list)
        for n, p in enumerate(parent):
            children[p].append(n)

        def dfs(node):
            result = 0
            childrenLength = []
            for child in children[node]:
                childResult, childLength = dfs(child)
                result = max(result, childResult)
                if s[node] == s[child]:
                    continue
                childrenLength.append(childLength)
            max1 = max2 = 0
            for l in childrenLength:
                if l > max1:
                    max2 = max1
                    max1 = l
                elif l > max2:
                    max2 = l
            return max(result, max1 + max2 + 1), max1 + 1

        return dfs(0)[0]
