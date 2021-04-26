# https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for level in range(1, len(triangle)):
            for index in range(level + 1):
                if index == 0:
                    triangle[level][index] += triangle[level - 1][index]
                elif index == level:
                    triangle[level][index] += triangle[level - 1][index - 1]
                else:
                    triangle[level][index] += min(triangle[level - 1][index], triangle[level - 1][index - 1])

        result = 2147483647
        for i in range(len(triangle)):
            if triangle[-1][i] < result:
                result = triangle[-1][i]

        return result
