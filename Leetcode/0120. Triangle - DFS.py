# https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.length = len(triangle[-1])
        self.triangle = triangle
        self.result = 2147483647

        self.dfs(0, 0, 0)

        return self.result

    def dfs(self, currentDepth, index, sum):
        if currentDepth == self.length:
            if sum < self.result:
                self.result = sum
            return
        self.dfs(currentDepth + 1, index, sum + self.triangle[currentDepth][index])
        if index < self.length - 1:
            self.dfs(currentDepth + 1, index + 1, sum + self.triangle[currentDepth][index])
