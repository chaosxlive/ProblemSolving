# https://leetcode.com/problems/high-five/

from collections import defaultdict


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        studentScores = defaultdict(lambda: [])
        for [studentId, score] in items:
            studentScores[studentId].append(score)
        result = []
        for studentId in studentScores.keys():
            scores = sorted(studentScores[studentId], reverse=True)
            result.append([studentId, sum(scores[:5]) // 5])
        return sorted(result, key=lambda x: x[0])
