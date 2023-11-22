# https://leetcode.com/problems/wildcard-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        idxS = 0
        idxSStar = 0
        idxP = 0
        idxStar = -1
        while idxS < len(s):
            if idxP < len(p) and (p[idxP] == '?' or p[idxP] == s[idxS]):
                idxS += 1
                idxP += 1
            elif idxP < len(p) and p[idxP] == '*':
                idxStar = idxP
                idxP += 1
                idxSStar = idxS
            elif idxStar != -1:
                idxP = idxStar + 1
                idxSStar += 1
                idxS = idxSStar
            else:
                return False
        while idxP < len(p) and p[idxP] == '*':
            idxP += 1
        return idxP == len(p)
