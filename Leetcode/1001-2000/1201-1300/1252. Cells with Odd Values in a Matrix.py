# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row = [0] * m
        col = [0] * n
        for index in indices:
            row[index[0]] += 1
            col[index[1]] += 1

        result = 0
        for r in row:
            for c in col:
                if (r + c) % 2 == 1:
                    result += 1
        return result
