# https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/

from math import ceil

class Solution:
    def twoEggDrop(self, n: int) -> int:
        return ceil((2 * n + 0.25) ** 0.5 - 0.5)