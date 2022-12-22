# https://leetcode.com/problems/campus-bikes-ii/

from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        self.result = 2147483647
        self.workers = workers
        self.bikes = bikes
        self.dfs(0, 0, 0)
        return self.result

    def dfs(self, currentWorkerIdx: int, pickedBikeBits: int, currentResult: int) -> None:
        workerX, workerY = self.workers[currentWorkerIdx]
        for idx, (bikeX, bikeY) in enumerate(self.bikes):
            bikeBit = 1 << idx
            if pickedBikeBits & bikeBit == 0:
                if currentWorkerIdx == len(self.workers) - 1:
                    self.result = min(self.result, currentResult + self.calDist(workerX, workerY, bikeX, bikeY))
                else:
                    self.dfs(currentWorkerIdx + 1, pickedBikeBits | bikeBit, currentResult + self.calDist(workerX, workerY, bikeX, bikeY))

    def calDist(self, x1: int, y1: int, x2: int, y2: int) -> int:
        return abs(x1 - x2) + abs(y1 - y2)

# TLE