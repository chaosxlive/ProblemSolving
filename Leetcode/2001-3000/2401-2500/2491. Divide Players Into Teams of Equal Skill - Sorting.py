# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        skillSum = sum(skill)
        skillAvg = skillSum / len(skill)
        target = skillAvg * 2
        result = 0
        for i in range(len(skill) // 2):
            if skill[i] + skill[-i - 1] != target:
                return -1
            result += skill[i] * skill[-i - 1]
        return result
