# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for row in range(1, numRows):
            result.append([1])
            for i in range(1, row):
                result[-1].append(result[row - 1][i - 1] + result[row - 1][i])
            result[-1].append(1)
        return result