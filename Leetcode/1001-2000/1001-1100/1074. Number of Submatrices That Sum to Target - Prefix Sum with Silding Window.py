# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        prefixSum = [[0] for i in range(len(matrix[0]))]
        for row in matrix:
            num = 0
            while num < len(matrix[0]):
                prefixSum[num].append(row[num] + prefixSum[num][-1])
                num += 1

        result = 0
        for upper in range(len(matrix)):
            for lower in range(upper, len(matrix)):
                occur_table = {
                    0: 1
                }
                currSum = 0
                for iter_index in range(len(matrix[0])):
                    currSum += prefixSum[iter_index][lower + 1] - prefixSum[iter_index][upper]
                    if currSum - target in occur_table:
                        result += occur_table[currSum - target]

                    if currSum in occur_table:
                        occur_table[currSum] += 1
                    else:
                        occur_table[currSum] = 1
        return result
