# https://leetcode.com/problems/spiral-matrix-iii/

from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, pr: int, pc: int) -> List[List[int]]:
        N = rows * cols
        result = [[pr, pc] for _ in range(N)]
        rest = N - 1
        step2 = 2  # times 2 for 2 dirs
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        while True:
            di = (step2 - 2) % 4
            step = step2 // 2
            for _ in range(step):
                if rest == 0:
                    return result
                dr, dc = dirs[di]
                pr += dr
                pc += dc
                if 0 <= pr < rows and 0 <= pc < cols:
                    result[N - rest] = [pr, pc]
                    rest -= 1
            step2 += 1
