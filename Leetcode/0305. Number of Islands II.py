# https://leetcode.com/problems/number-of-islands-ii/

from typing import List


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        uf = {}

        def find(x):
            if x not in uf:
                uf[x] = x
            elif uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                uf[rx] = ry
                return True
            return False

        islandCnt = 0
        result = []
        for r, c in positions:
            if (r, c) not in uf:
                find((r, c))
                islandCnt += 1
                for dr, dc in dirs:
                    if 0 <= r + dr < m and 0 <= c + dc < n and (r + dr, c + dc) in uf and union((r, c), (r + dr, c + dc)):
                        islandCnt -= 1
            result.append(islandCnt)
        return result
