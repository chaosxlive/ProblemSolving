# https://leetcode.com/problems/water-bottles-ii/

class Solution:

    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk = 0
        result = 0
        while numBottles > 0:
            result += numBottles
            drunk += numBottles
            numBottles = 0
            while drunk >= numExchange:
                drunk -= numExchange
                numBottles += 1
                numExchange += 1
        return result
