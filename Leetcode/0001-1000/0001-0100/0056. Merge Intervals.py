# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        index = 1
        while index < len(intervals):
            if intervals[index - 1][0] <= intervals[index][0] <= intervals[index - 1][1]:
                intervals[index - 1][1] = max(intervals[index - 1][1], intervals[index][1])
                del intervals[index]
            else:
                index += 1
        return intervals
