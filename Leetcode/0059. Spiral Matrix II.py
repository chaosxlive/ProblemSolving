# https://leetcode.com/problems/spiral-matrix-ii/

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        wallLeft, wallRight, wallTop, wallBottom = -1, n, 0, n
        x, y = 0, 0
        result = [[1] * n for i in range(n)]
        d = 0  # 0: right, 1: down, 2: left, 3: up
        c = 2
        while True:
            if d == 0:
                if x + 1 < wallRight:
                    x += 1
                    result[y][x] = c
                    c += 1
                elif y + 1 < wallBottom:
                    wallRight = x
                    d = 1
                else:
                    break
            elif d == 1:
                if y + 1 < wallBottom:
                    y += 1
                    result[y][x] = c
                    c += 1
                elif x - 1 > wallLeft:
                    wallBottom = y
                    d = 2
                else:
                    break
            elif d == 2:
                if x - 1 > wallLeft:
                    x -= 1
                    result[y][x] = c
                    c += 1
                elif y - 1 > wallTop:
                    wallLeft = x
                    d = 3
                else:
                    break
            else:
                if y - 1 > wallTop:
                    y -= 1
                    result[y][x] = c
                    c += 1
                elif x + 1 < wallRight:
                    wallTop = y
                    d = 0
                else:
                    break
        return result
