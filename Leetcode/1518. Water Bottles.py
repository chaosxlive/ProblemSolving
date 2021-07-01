# https://leetcode.com/problems/water-bottles/

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = 0
        bottleNew, bottleEmpty = numBottles, 0
        while bottleNew > 0:
            result += bottleNew
            bottleEmpty += bottleNew
            bottleNew = bottleEmpty // numExchange
            bottleEmpty %= numExchange
        return result
