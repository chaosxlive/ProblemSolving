# https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedHeights = sorted(heights)

        result = 0
        for i in range(len(heights)):
            if sortedHeights[i] != heights[i]:
                result += 1
        
        return result