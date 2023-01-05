# https://leetcode.com/problems/k-closest-points-to-origin/

from typing import List
from random import randint
from math import sqrt


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.result = []
        self.points = list(map(lambda p: (sqrt(p[0] * p[0] + p[1] * p[1]), [p[0], p[1]]), points))
        self.k = k

        self.quickSelect()

        return self.result

    def quickSelect(self):
        pivotIdx = randint(0, len(self.points) - 1)
        pivotDist, pivotPoint = self.points[pivotIdx]
        left = []
        right = []
        for point in self.points:
            if point[0] <= pivotDist:
                left.append(point)
            else:
                right.append(point)
        if len(self.result) + len(left) > self.k:
            self.points = left
            self.quickSelect()
        elif len(self.result) + len(left) < self.k:
            self.result.extend(map(lambda x: x[1], left))
            self.points = right
            self.quickSelect()
        else:
            self.result.extend(map(lambda x: x[1], left))
