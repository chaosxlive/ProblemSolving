# https://leetcode.com/problems/sort-the-students-by-their-kth-score/

from typing import List


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, reverse=True, key=lambda x: x[k])
