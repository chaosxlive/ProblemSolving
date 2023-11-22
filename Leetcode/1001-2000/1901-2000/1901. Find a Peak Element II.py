# https://leetcode.com/problems/find-a-peak-element-ii/

from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        row = col = 0
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while True:
            isNext = False
            for dr, dc in dirs:
                if 0 <= row + dr < len(mat) and 0 <= col + dc < len(mat[0]):
                    if mat[row + dr][col + dc] > mat[row][col]:
                        row += dr
                        col += dc
                        isNext = True
                        break
            if not isNext:
                return [row, col]
