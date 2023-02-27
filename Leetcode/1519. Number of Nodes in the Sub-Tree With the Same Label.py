# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

from typing import List
from collections import defaultdict


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        nextNodes = defaultdict(list)
        for x, y in edges:
            nextNodes[x].append(y)
            nextNodes[y].append(x)

        result = [0] * n

        def dfs(node, parent):
            counter = [0] * 26
            for nextNode in nextNodes[node]:
                if nextNode != parent:
                    childCounter = dfs(nextNode, node)
                    counter = list(map(sum, zip(counter, childCounter)))
            num = ord(labels[node]) - 97
            counter[num] += 1
            result[node] = counter[num]
            return counter

        dfs(0, -1)
        return result
