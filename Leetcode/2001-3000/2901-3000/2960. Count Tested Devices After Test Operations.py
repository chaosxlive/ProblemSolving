# https://leetcode.com/problems/count-tested-devices-after-test-operations/

from typing import List


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        result = 0
        for b in batteryPercentages:
            if b - result > 0:
                result += 1
        return result
