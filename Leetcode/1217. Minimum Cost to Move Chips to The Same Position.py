# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        countOdd = countEven = 0
        for pos in position:
            if pos % 2 == 0:
                countEven += 1
            else:
                countOdd += 1
            
        return min(countEven, countOdd)