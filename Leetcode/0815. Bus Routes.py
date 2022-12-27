# https://leetcode.com/problems/bus-routes/

from typing import List
from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stops = defaultdict(list)
        for routeId, route in enumerate(routes):
            for stopId in route:
                stops[stopId].append(routeId)
        stopQueue = deque([(source, 0)])
        seenRoute = set()
        seenStop = set([source])
        while stopQueue:
            stopId, step = stopQueue.popleft()
            if stopId == target:
                return step
            stopRoutes = stops[stopId]
            for routeId in stopRoutes:
                if routeId not in seenRoute:
                    seenRoute.add(routeId)
                    for stop in routes[routeId]:
                        if stop not in seenStop:
                            seenStop.add(stop)
                            stopQueue.append((stop, step + 1))
        return -1
