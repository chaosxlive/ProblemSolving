# https://leetcode.com/problems/minimum-costs-using-the-train-line/

from typing import List


class Solution:

    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        L = len(regular)
        timeReg, timeExp = 0, expressCost
        result = [0] * L
        for i in range(L):
            timeReg, timeExp = min(timeReg + regular[i], timeExp + regular[i]), min(timeReg + expressCost + express[i], timeExp + express[i])
            result[i] = min(timeReg, timeExp)
        return result
