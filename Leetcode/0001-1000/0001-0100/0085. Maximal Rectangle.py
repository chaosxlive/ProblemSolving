# https://leetcode.com/problems/maximal-rectangle/

from typing import List


class Solution:

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heights = [list(map(int, R)) for R in matrix]
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    heights[i][j] += heights[i - 1][j]

        def largestRectangleArea(heights: List[int]) -> int:
            L = len(heights)
            stack = [-1]
            result = 0
            for i, h in enumerate(heights):
                while len(stack) > 1 and heights[stack[-1]] >= h:
                    result = max(result, heights[stack.pop()] * (i - stack[-1] - 1))
                stack.append(i)
            while len(stack) > 1:
                result = max(result, heights[stack.pop()] * (L - stack[-1] - 1))
            return result

        return max(largestRectangleArea(R) for R in heights)
