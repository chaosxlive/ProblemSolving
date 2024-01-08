# https://leetcode.com/problems/brightest-position-on-street/

from heapq import heappop, heappush
from typing import List


class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        lArr = sorted([p - r, p + r] for p, r in lights)
        resultVal = -1
        resultPos = -2147483648
        dq = []
        for ls, le in lArr:
            while len(dq) and dq[0] < ls:
                heappop(dq)
            heappush(dq, le)
            if len(dq) > resultVal:
                resultVal = len(dq)
                resultPos = ls
        return resultPos
