# https://leetcode.com/problems/24-game/

from itertools import permutations
from math import isclose


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        if len(cards) == 1:
            return isclose(cards[0], 24)
        for a, b, *others in permutations(cards):
            if self.judgePoint24([a + b] + others):
                return True
            if self.judgePoint24([a - b] + others):
                return True
            if self.judgePoint24([a * b] + others):
                return True
            if b != 0 and self.judgePoint24([a / b] + others):
                return True
        return False
