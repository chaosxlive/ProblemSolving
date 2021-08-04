# https://leetcode.com/problems/search-a-2d-matrix/

from bisect import bisect


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        row = bisect([row[0] for row in matrix], target) - 1
        if target < matrix[row][0] or target > matrix[row][-1]:
            return False
        return matrix[row][bisect(matrix[row], target) - 1] == target
