# https://leetcode.com/problems/maximum-compatibility-score-sum/

from itertools import permutations


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        result = 0
        pairs = list(permutations(n for n in range(len(students))))
        for pair in pairs:
            temp = 0
            for i in range(len(students)):
                student = students[i]
                mentor = mentors[pair[i]]
                for i in range(len(student)):
                    temp += 1 if student[i] == mentor[i] else 0
            result = max(result, temp)
        return result
