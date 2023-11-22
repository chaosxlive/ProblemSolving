# https://leetcode.com/problems/number-of-visible-people-in-a-queue/

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        result = [0] * len(heights)
        stack = [heights[-1]]
        for i in range(len(heights) - 2, -1, -1):
            origin = len(stack)
            while len(stack) and heights[i] > stack[-1]:
                stack.pop()
            result[i] = origin - len(stack)
            if len(stack):
                result[i] += 1
            stack.append(heights[i])
        return result
