# https://leetcode.com/problems/distance-between-bus-stops/

from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = 0
        path = 0
        start, destination = min(start, destination), max(start, destination)
        for i, d in enumerate(distance):
            total += d
            if start <= i < destination:
                path += d
        return min(path, total - path)
