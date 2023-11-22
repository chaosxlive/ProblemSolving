# https://leetcode.com/problems/find-the-winner-of-an-array-game/

from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k == 1:
            return max(arr[0], arr[1])
        a = arr[0]
        winCnt = 0
        for i in range(1, len(arr)):
            b = arr[i]
            if a > b:
                winCnt += 1
                if winCnt == k:
                    return a
            else:
                a = b
                winCnt = 1
        return max(arr)
