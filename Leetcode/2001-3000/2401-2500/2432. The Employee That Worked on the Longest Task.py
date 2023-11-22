# https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        prevEnd = 0
        resultId = -1
        resultLength = 0
        for eId, time in logs:
            if time - prevEnd > resultLength:
                resultLength = time - prevEnd
                resultId = eId
            elif time - prevEnd == resultLength and eId < resultId:
                resultId = eId
            prevEnd = time
        return resultId
