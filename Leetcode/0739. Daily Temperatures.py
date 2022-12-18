# https://leetcode.com/problems/daily-temperatures/

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            while len(stack) > 0 and temperatures[i] >= stack[-1][0]:
                stack.pop()
            if len(stack) > 0:
                result[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        return result
