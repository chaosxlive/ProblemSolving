# https://leetcode.com/problems/heaters/

from bisect import bisect_left


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        minRadius = 0
        for house in houses:
            index = bisect_left(heaters, house)
            if index == 0:
                minRadius = max(minRadius, heaters[0] - house)
            elif index == len(heaters):
                minRadius = max(minRadius, house - heaters[-1])
            else:
                minRadius = max(minRadius, min(heaters[index] - house, house - heaters[index - 1]))
        return minRadius
