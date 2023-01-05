# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

from typing import List
from collections import deque


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        restBalloons = deque(sorted(points))
        result = 0
        while restBalloons:
            result += 1
            _, possibleX = restBalloons.popleft()
            while restBalloons:
                peekNextStart, peekNextEnd = restBalloons[0]
                if possibleX >= peekNextStart:
                    possibleX = min(possibleX, peekNextEnd)
                    restBalloons.popleft()
                else:
                    break
        return result
