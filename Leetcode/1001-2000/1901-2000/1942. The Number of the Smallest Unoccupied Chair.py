# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

import heapq


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        chairs = [i for i in range(len(times))]
        heapq.heapify(chairs)
        items = [(times[i][0], True, i) for i in range(len(times))] + [(times[i][1], False, i) for i in range(len(times))]
        items.sort()
        sit = {}
        for time, isArrived, id in items:
            if isArrived:
                if id == targetFriend:
                    return heapq.heappop(chairs)
                sit[id] = heapq.heappop(chairs)
            else:
                heapq.heappush(chairs, sit[id])
