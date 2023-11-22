# https://leetcode.com/problems/non-overlapping-intervals/

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        result = 0
        lastPicked = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < lastPicked[1]:
                result += 1
            else:
                lastPicked = intervals[i]
        return result
