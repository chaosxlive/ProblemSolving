# https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        lines = len(mat) + len(mat[0]) - 1
        result = []
        for line in range(lines):
            if line % 2 == 0:
                if line >= len(mat):
                    row, col = len(mat) - 1, line - len(mat) + 1
                else:
                    row, col = line, 0
                while col < len(mat[0]) and row >= 0:
                    result.append(mat[row][col])
                    row -= 1
                    col += 1
            else:
                if line >= len(mat[0]):
                    row, col = line - len(mat[0]) + 1, len(mat[0]) - 1
                else:
                    row, col = 0, line
                while row < len(mat) and col >= 0:
                    result.append(mat[row][col])
                    row += 1
                    col -= 1

        return result
