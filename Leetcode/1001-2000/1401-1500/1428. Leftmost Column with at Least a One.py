# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#     def get(self, row: int, col: int) -> int:
#     def dimensions(self) -> list[]:


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rowSize, colSize = binaryMatrix.dimensions()
        result = colSize
        for rowIdx in range(rowSize):
            left, right = 0, result - 1
            oneIdx = -1
            while left <= right:
                mid = left + (right - left) // 2
                if binaryMatrix.get(rowIdx, mid) == 1:
                    oneIdx = mid
                    right = mid - 1
                else:
                    left = mid + 1
            if oneIdx != -1:
                result = oneIdx
        return -1 if result == colSize else result
