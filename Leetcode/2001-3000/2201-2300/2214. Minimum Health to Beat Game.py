# https://leetcode.com/problems/minimum-health-to-beat-game/

from typing import List


class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        total = 0
        maxDamage = 0
        for d in damage:
            total += d
            maxDamage = max(maxDamage, d)
        return total - min(armor, maxDamage) + 1
