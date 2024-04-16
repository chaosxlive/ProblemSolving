# https://leetcode.com/problems/campus-bikes-ii/

from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        self.workers = workers
        self.bikes = bikes
        self.bitBest = {}
        return self.dfs(0, 0)

    def dfs(self, currentWorkerIdx: int, pickedBikeBits: int) -> int:
        if currentWorkerIdx == len(self.workers):
            return 0
        if pickedBikeBits in self.bitBest:
            return self.bitBest[pickedBikeBits]
        workerX, workerY = self.workers[currentWorkerIdx]
        currentBest = 2147483647
        for idx, (bikeX, bikeY) in enumerate(self.bikes):
            bikeBit = 1 << idx
            if pickedBikeBits & bikeBit == 0:
                currentBest = min(currentBest, self.dfs(currentWorkerIdx + 1, pickedBikeBits | bikeBit) + self.calDist(workerX, workerY, bikeX, bikeY))
        self.bitBest[pickedBikeBits] = currentBest
        return currentBest

    def calDist(self, x1: int, y1: int, x2: int, y2: int) -> int:
        return abs(x1 - x2) + abs(y1 - y2)
