# https://leetcode.com/problems/minimum-number-of-refueling-stops/

import heapq


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        maxDistance = startFuel
        validStations = []
        result = 0
        index = 0
        while True:
            while index < len(stations) and stations[index][0] <= maxDistance:
                heapq.heappush(validStations, -stations[index][1])
                index += 1
            if maxDistance >= target:
                return result
            if len(validStations) == 0:
                return -1
            maxDistance -= heapq.heappop(validStations)
            result += 1
