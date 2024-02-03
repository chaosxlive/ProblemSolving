# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/

from typing import List


class Solution:

    def numberOfPairs(self, points: List[List[int]]) -> int:
        L = len(points)
        points.sort(key=lambda x: (x[0], -x[1]))
        result = 0
        for i in range(L - 1):
            p1 = points[i]
            j = i + 1
            while j < L:
                if points[j][1] > p1[1]:
                    j += 1
                    continue
                result += 1
                break
            k = j + 1
            while k < L:
                if points[k][1] <= p1[1] and points[k][1] > points[j][1]:
                    result += 1
                    j = k
                k += 1

        return result
