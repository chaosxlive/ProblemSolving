# https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currentHeight = 0
        highest = 0

        for dif in gain:
            currentHeight += dif
            if currentHeight > highest:
                highest = currentHeight

        return highest
