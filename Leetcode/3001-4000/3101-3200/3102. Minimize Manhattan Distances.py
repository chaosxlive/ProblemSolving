# https://leetcode.com/problems/minimize-manhattan-distances/

from math import inf
from typing import List


class Solution:

    def minimumDistance(self, points: List[List[int]]) -> int:
        L = len(points)
        result = inf
        ignores = [0] * 4

        for t in range(5):
            start = 0 if t == 0 else (1 if ignores[t - 1] == 0 else 0)
            minSum = maxSum = points[start][0] + points[start][1]
            minDiff = maxDiff = points[start][0] - points[start][1]

            for i in range(1, L):
                if t > 0 and i == ignores[t - 1]:
                    continue
                currSum = points[i][0] + points[i][1]
                currDiff = points[i][0] - points[i][1]
                if (currSum < minSum):
                    minSum = currSum
                    if t == 0:
                        ignores[0] = i
                elif (currSum > maxSum):
                    maxSum = currSum
                    if t == 0:
                        ignores[1] = i
                if (currDiff < minDiff):
                    minDiff = currDiff
                    if t == 0:
                        ignores[2] = i
                elif (currDiff > maxDiff):
                    maxDiff = currDiff
                    if t == 0:
                        ignores[3] = i
            result = min(result, max(maxSum - minSum, maxDiff - minDiff))

        return result
