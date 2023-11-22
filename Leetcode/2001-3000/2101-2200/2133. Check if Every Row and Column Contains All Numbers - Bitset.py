# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        rowCheck = [0] * n
        colCheck = [0] * n
        for row in range(n):
            for col in range(n):
                mask = 1 << matrix[row][col]
                if mask & rowCheck[row] or mask & colCheck[col]:
                    return False
                rowCheck[row] |= mask
                colCheck[col] |= mask

        expected = 2**(n + 1) - 2
        for checks in rowCheck:
            if checks != expected:
                return False
        for checks in colCheck:
            if checks != expected:
                return False
        return True