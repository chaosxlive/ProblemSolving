# https://leetcode.com/problems/stone-game-vi/

from typing import List


class Solution:

    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        vs = sorted(map(lambda x: (x[0] + x[1], x[0], x[1]), zip(aliceValues, bobValues)), reverse=True)
        a = sum(map(lambda x: x[1], vs[::2]))
        b = sum(map(lambda x: x[2], vs[1::2]))
        if a > b:
            return 1
        if a < b:
            return -1
        return 0
