# https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        result = []
        for x in range(1, 1001):
            left, right = 1, 1001
            while left < right:
                isLast = left == right - 1
                y = (left + right) // 2
                ret = customfunction.f(x, y)
                if ret < z:
                    left = y + 1
                elif ret > z:
                    right = y
                else:
                    result.append([x, y])
                    break
                if isLast:
                    break
        return result
