# https://leetcode.com/problems/design-underground-system/

from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.passengers = {}
        self.travelTime = defaultdict(lambda: 0)
        self.travelCount = defaultdict(lambda: 0)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passengers[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.travelTime[(self.passengers[id][1], stationName)] += t - self.passengers[id][0]
        self.travelCount[(self.passengers[id][1], stationName)] += 1
        self.passengers.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.travelTime[(startStation, endStation)] / self.travelCount[(startStation, endStation)]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
