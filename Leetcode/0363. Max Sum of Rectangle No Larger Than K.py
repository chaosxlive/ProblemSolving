# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        prefixSum = [[0 for col in range(len(matrix[0]) + 1)] for row in range(len(matrix) + 1)]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                prefixSum[row + 1][col + 1] = matrix[row][col] - prefixSum[row][col] + prefixSum[row][col + 1] + prefixSum[row + 1][col]

        result = -2147483648
        for rowUpper in range(len(matrix)):
            for colLeft in range(len(matrix[0])):
                for rowLower in range(rowUpper, len(matrix)):
                    for colRight in range(colLeft, len(matrix[0])):
                        currentSum = prefixSum[rowLower + 1][colRight + 1] - prefixSum[rowUpper][colRight + 1] - prefixSum[rowLower + 1][colLeft] + prefixSum[rowUpper][colLeft]
                        if currentSum <= k:
                            result = max(result, currentSum)
        return result

# TLE