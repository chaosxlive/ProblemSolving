# https://leetcode.com/problems/last-day-where-you-can-still-cross/

from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        isLand = [False] * (col * (row + 2))
        uf = {}

        for idxF in range(col):
            idxB = len(isLand) - idxF - 1
            isLand[idxF] = True
            isLand[idxB] = True
            uf[idxF] = -1
            uf[idxB] = 2147483647

        def getIdx(r: int, c: int):
            return r * col + c - 1

        def find(x):
            if x not in uf:
                uf[x] = x
            elif uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                if rx > ry:
                    uf[ry] = rx
                else:
                    uf[rx] = ry

        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        for i in range(len(cells) - 1, -1, -1):
            r, c = cells[i]
            idxCurrent = getIdx(r, c)
            isLand[idxCurrent] = True
            find(idxCurrent)
            for dr, dc in dirs:
                if 0 > c - 1 + dc or c - 1 + dc >= col:
                    continue
                idxNeighbor = getIdx(r + dr, c + dc)
                if 0 <= idxNeighbor < len(isLand) and isLand[idxNeighbor]:
                    union(idxCurrent, idxNeighbor)
            if find(0) == find(len(isLand) - 1):
                return i
        return 0
