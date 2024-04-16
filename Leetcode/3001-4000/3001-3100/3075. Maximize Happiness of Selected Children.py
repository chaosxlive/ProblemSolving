# https://leetcode.com/problems/maximize-happiness-of-selected-children/

from typing import List


class Solution:

    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        result = 0
        for i, happy in enumerate(happiness[:k]):
            result += max(happy - i, 0)
        return result
