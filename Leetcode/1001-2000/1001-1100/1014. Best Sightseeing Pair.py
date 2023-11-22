# https://leetcode.com/problems/best-sightseeing-pair/

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        prevMax = None
        result = -1
        for i in range(len(values) - 1, -1, -1):
            valueAddIndex = values[i] + i
            valueMinusIndex = values[i] - i
            if prevMax is not None:
                result = max(result, valueAddIndex + prevMax)
                prevMax = max(prevMax, valueMinusIndex)
            else:
                prevMax = valueMinusIndex
        return result
