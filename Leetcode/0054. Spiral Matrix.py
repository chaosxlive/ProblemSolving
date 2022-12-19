# https://leetcode.com/problems/spiral-matrix/

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        wallLeft, wallRight, wallTop, wallBottom = -1, len(matrix[0]), 0, len(matrix)
        x, y = 0, 0
        result = [matrix[0][0]]
        d = 0  # 0: right, 1: down, 2: left, 3: up
        while True:
            if d == 0:
                if x + 1 < wallRight:
                    x += 1
                    result.append(matrix[y][x])
                elif y + 1 < wallBottom:
                    wallRight = x
                    d = 1
                else:
                    break
            elif d == 1:
                if y + 1 < wallBottom:
                    y += 1
                    result.append(matrix[y][x])
                elif x - 1 > wallLeft:
                    wallBottom = y
                    d = 2
                else:
                    break
            elif d == 2:
                if x - 1 > wallLeft:
                    x -= 1
                    result.append(matrix[y][x])
                elif y - 1 > wallTop:
                    wallLeft = x
                    d = 3
                else:
                    break
            else:
                if y - 1 > wallTop:
                    y -= 1
                    result.append(matrix[y][x])
                elif x + 1 < wallRight:
                    wallTop = y
                    d = 0
                else:
                    break
        return result
