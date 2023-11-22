# https://leetcode.com/problems/meeting-rooms-ii/

from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ends = []
        result = 1
        for start, end in intervals:
            while len(ends) > 0 and ends[0] <= start:
                heapq.heappop(ends)
            result = max(result, len(ends) + 1)
            heapq.heappush(ends, end)
        return result
