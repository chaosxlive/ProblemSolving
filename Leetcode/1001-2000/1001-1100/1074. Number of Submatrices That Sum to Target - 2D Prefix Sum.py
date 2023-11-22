# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        height, width = len(matrix), len(matrix[0])
        prefixSum = [[0 for x in range(width + 1)] for y in range(height + 1)]
        for i in range(height):
            for j in range(width):
                prefixSum[i + 1][j + 1] = matrix[i][j] + prefixSum[i + 1][j] + prefixSum[i][j + 1] - prefixSum[i][j]

        count = 0
        for x1 in range(height):
            for y1 in range(width):
                for x2 in range(x1, height):
                    for y2 in range(y1, width):
                        if prefixSum[x2+1][y2+1] + prefixSum[x1][y1] - prefixSum[x2+1][y1] - prefixSum[x1][y2+1] == target:
                            count += 1

        return count
