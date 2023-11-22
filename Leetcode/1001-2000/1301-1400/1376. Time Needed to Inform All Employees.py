# https://leetcode.com/problems/time-needed-to-inform-all-employees/

from typing import List
from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = defaultdict(list)
        for i, m in enumerate(manager):
            subordinates[m].append(i)

        def dfs(m, t):
            result = t
            for sub in subordinates[m]:
                result = max(result, dfs(sub, t + informTime[m]))
            return result

        return dfs(headID, 0)
