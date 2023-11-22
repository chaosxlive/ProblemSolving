# https://leetcode.com/problems/find-the-winner-of-an-array-game/

from typing import List
from collections import deque


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k == 1:
            return max(arr[0], arr[1])
        dq = deque(arr)
        a = dq.popleft()
        winCnt = 0
        while len(dq) > 0:
            b = dq.popleft()
            if a > b:
                winCnt += 1
                if winCnt == k:
                    return a
            else:
                a = b
                winCnt = 1
        return max(arr)
