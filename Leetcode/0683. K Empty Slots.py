# https://leetcode.com/problems/k-empty-slots/

from typing import List
from bisect import bisect


class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        bulbOn = []
        for day, bulb in enumerate(bulbs):
            idx = bisect(bulbOn, bulb)
            bulbOn.insert(idx, bulb)
            if idx >= 1 and bulb - bulbOn[idx - 1] == k + 1:
                return day + 1
            if idx < len(bulbOn) - 1 and bulbOn[idx + 1] - bulb == k + 1:
                return day + 1
        return -1
