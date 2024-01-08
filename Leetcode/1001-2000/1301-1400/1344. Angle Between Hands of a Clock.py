# https://leetcode.com/problems/angle-between-hands-of-a-clock/

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        result = abs((6 * minutes) - (30 * hour + minutes / 2))
        return 360 - result if result > 180 else result
