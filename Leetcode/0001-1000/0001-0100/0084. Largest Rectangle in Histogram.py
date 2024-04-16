# https://leetcode.com/problems/largest-rectangle-in-histogram/

from typing import List


class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
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
