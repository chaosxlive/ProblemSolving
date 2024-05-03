from typing import List, Optional


class Solution:

    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i in range(2):
            for j in range(2):
                cnt = 0
                if grid[i][j] == 'B':
                    cnt += 1
                else:
                    cnt -= 1
                if grid[i + 1][j] == 'B':
                    cnt += 1
                else:
                    cnt -= 1
                if grid[i][j + 1] == 'B':
                    cnt += 1
                else:
                    cnt -= 1
                if grid[i + 1][j + 1] == 'B':
                    cnt += 1
                else:
                    cnt -= 1
                if cnt != 0:
                    return True
        return False
