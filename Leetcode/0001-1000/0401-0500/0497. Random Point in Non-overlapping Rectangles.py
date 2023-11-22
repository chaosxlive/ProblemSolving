# https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/

import random


class Solution:

    def __init__(self, rects: List[List[int]]):

        def getIntPointCounts(x1, y1, x2, y2):
            return (x2 - x1 + 1) * (y2 - y1 + 1)

        totalPoints = 0
        for rect in rects:
            totalPoints += getIntPointCounts(rect[0], rect[1], rect[2], rect[3])
        self.rects = []
        pointsUsed = 0.0
        for rect in rects:
            pointCount = getIntPointCounts(rect[0], rect[1], rect[2], rect[3])
            pointsUsed += pointCount / totalPoints
            self.rects.append((pointsUsed, pointCount, tuple(rect)))

    def pick(self) -> List[int]:
        pickedRect = random.uniform(0, 1)
        for i in range(len(self.rects)):
            if pickedRect <= self.rects[i][0]:
                pickedRect = self.rects[i]
                break
        pickedPoint = random.randint(0, pickedRect[1] - 1)
        rowPoints = pickedRect[2][2] - pickedRect[2][0] + 1
        return [pickedRect[2][0] + pickedPoint % rowPoints, pickedRect[2][1] + pickedPoint // rowPoints]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
