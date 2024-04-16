# https://leetcode.com/problems/valid-parenthesis-string/


class Solution:

    def checkValidString(self, s: str) -> bool:
        cntMin, cntMax = 0, 0
        for c in s:
            cntMin = max(cntMin + 1 if c == '(' else cntMin - 1, 0)
            cntMax = cntMax - 1 if c == ')' else cntMax + 1
            if cntMax < 0:
                return False
        return cntMin == 0
