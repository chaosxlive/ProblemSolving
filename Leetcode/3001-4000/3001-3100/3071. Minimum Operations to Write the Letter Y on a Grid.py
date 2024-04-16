# https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/

from typing import List


class Solution:

    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        L = len(grid)
        CN = L // 2
        result = 2147483647
        for outNum in range(3):
            for inNum in range(3):
                if outNum == inNum:
                    continue
                cnt = 0
                for r in range(L):
                    for c in range(L):
                        if r < CN and r == c:
                            if grid[r][c] != inNum:
                                cnt += 1
                            continue
                        if r < CN and r + c == L - 1:
                            if grid[r][c] != inNum:
                                cnt += 1
                            continue
                        if r > CN and c == CN:
                            if grid[r][c] != inNum:
                                cnt += 1
                            continue
                        if r == CN and c == CN:
                            if grid[r][c] != inNum:
                                cnt += 1
                            continue
                        if grid[r][c] != outNum:
                            cnt += 1
                result = min(result, cnt)
        return result
