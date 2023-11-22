# https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/

from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        addedExperience = 0
        currentExperience = initialExperience
        for enemyExperience in experience:
            if currentExperience < enemyExperience + 1:
                addedExperience += enemyExperience + 1 - currentExperience
                currentExperience = 2 * enemyExperience + 1
            else:
                currentExperience += enemyExperience
        return max(0, sum(energy) + 1 - initialEnergy) + addedExperience
