# https://leetcode.com/problems/add-minimum-number-of-rungs/

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        current = 0
        result = 0
        for h in rungs:
            if h - current > dist:
                result += (h - current - dist - 1) // dist + 1
            current = h
        return result
