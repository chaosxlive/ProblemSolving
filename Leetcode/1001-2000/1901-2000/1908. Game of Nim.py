# https://leetcode.com/problems/game-of-nim/

from typing import List
from functools import reduce
from operator import xor


class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        return reduce(xor, piles) != 0
