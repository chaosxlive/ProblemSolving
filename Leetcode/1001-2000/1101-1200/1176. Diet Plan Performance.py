# https://leetcode.com/problems/diet-plan-performance/

from typing import List


class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        score = 0
        s = sum(calories[:k - 1])
        for i in range(len(calories) - k + 1):
            s += calories[k + i - 1]
            if s > upper:
                score += 1
            elif s < lower:
                score -= 1
            s -= calories[i]
        return score
