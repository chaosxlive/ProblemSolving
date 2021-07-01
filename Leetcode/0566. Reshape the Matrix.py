# https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        result = [[0 for col in range(c)] for row in range(r)]
        index = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                result[index // c][index % c] = mat[row][col]
                index += 1
        return result
