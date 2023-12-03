# https://leetcode.com/problems/maximum-distance-in-arrays/

from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        curMax, curMin, result = arrays[0][-1], arrays[0][0], 0
        for i in range(1, len(arrays)):
            result = max(result, abs(arrays[i][0] - curMax), abs(arrays[i][-1] - curMin))
            curMax = max(curMax, arrays[i][-1])
            curMin = min(curMin, arrays[i][0])
        return result
