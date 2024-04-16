# https://leetcode.com/problems/buildings-with-an-ocean-view/

from typing import List


class Solution:

    def findBuildings(self, heights: List[int]) -> List[int]:
        result = []
        M = 0
        for i in reversed(range(len(heights))):
            if heights[i] > M:
                result.append(i)
                M = heights[i]
        return result[::-1]
