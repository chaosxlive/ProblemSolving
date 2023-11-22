# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

from collections import defaultdict


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skillSum = sum(skill)
        target = (skillSum / len(skill)) * 2
        if int(target) != target:
            return -1
        target = int(target)
        candidates = defaultdict(int)
        candidateCnt = 0
        result = 0
        for s in skill:
            if candidates[target - s] > 0:
                candidates[target - s] -= 1
                candidateCnt -= 1
                result += s * (target - s)
            else:
                candidates[s] += 1
                candidateCnt += 1
        return -1 if candidateCnt > 0 else result
