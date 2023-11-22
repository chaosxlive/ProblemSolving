# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

from typing import List
from collections import Counter


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        taskCounter = Counter(tasks)
        result = 0
        for taskCnt in taskCounter.values():
            if taskCnt == 1:
                return -1
            result += taskCnt // 3 if taskCnt % 3 == 0 else taskCnt // 3 + 1
        return result
