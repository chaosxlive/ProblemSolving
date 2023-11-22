# https://leetcode.com/problems/campus-bikes/

from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        candidates = [(abs(workerX - bikeX) + abs(workerY - bikeY), workerIdx, bikeIdx) for workerIdx, (workerX, workerY) in enumerate(workers) for bikeIdx, (bikeX, bikeY) in enumerate(bikes)]
        candidates.sort()
        result = [-1] * len(workers)
        assignedBike = set()
        for distance, workerId, bikeId in candidates:
            if result[workerId] == -1 and bikeId not in assignedBike:
                result[workerId] = bikeId
                assignedBike.add(bikeId)
        return result
