# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        result = set(i for i in range(n))
        for start, end in edges:
            if end in result:
                result.remove(end)
        return list(result)
