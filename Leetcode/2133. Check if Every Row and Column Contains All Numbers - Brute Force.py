# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        cmatrix = [[row[col] for row in matrix] for col in range(n)]
        for i in range(1, n + 1):
            for row in matrix:
                if i not in row:
                    return False
            for col in cmatrix:
                if i not in col:
                    return False
        return True
