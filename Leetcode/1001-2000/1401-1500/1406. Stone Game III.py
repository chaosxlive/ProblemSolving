# https://leetcode.com/problems/stone-game-iii/

from typing import List


class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        L = len(stoneValue)
        self.result = [None] * L

        def solve(i: int):
            if i >= L:
                return 0
            elif self.result[i] is not None:
                return self.result[i]
            self.result[i] = max(sum(stoneValue[i:i + l]) - solve(i + l) for l in range(1, 4))
            return self.result[i]

        result = max(sum(stoneValue[:l]) - solve(l) for l in range(1, 4))
        if result > 0:
            return 'Alice'
        if result < 0:
            return 'Bob'
        return 'Tie'
