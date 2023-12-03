# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

from typing import List


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()

        c = 1
        mh = 1
        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i - 1] + 1:
                c += 1
                mh = max(mh, c)
            else:
                c = 1
        c = 1
        mv = 1
        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i - 1] + 1:
                c += 1
                mv = max(mv, c)
            else:
                c = 1
        return (min(mh, mv) + 1) ** 2
