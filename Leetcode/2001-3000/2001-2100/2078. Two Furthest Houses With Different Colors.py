# https://leetcode.com/problems/two-furthest-houses-with-different-colors/

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        result = 0
        for i in range(len(colors) - 1):
            for j in range(i + 1, len(colors)):
                if colors[i] != colors[j]:
                    result = max(result, abs(i - j))
        return result
