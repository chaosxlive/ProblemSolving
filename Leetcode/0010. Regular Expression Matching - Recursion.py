# https://leetcode.com/problems/regular-expression-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.s = s
        self.p = p
        self.lenS = len(s)
        self.lenP = len(p)

        return self.check(0, 0)

    def check(self, startS, startP):
        if startP == self.lenP:
            return startS == self.lenS

        if startP + 1 == self.lenP:
            return startS + 1 == self.lenS and (self.p[startP] == '.' or self.p[startP] == self.s[startS])

        if self.p[startP + 1] != '*':
            if startS == self.lenS:
                return False
            return (self.p[startP] == '.' or self.p[startP] == self.s[startS]) and self.check(startS + 1, startP + 1)

        while startS != self.lenS and (self.p[startP] == '.' or self.p[startP] == self.s[startS]):
            if self.check(startS, startP + 2):
                return True
            startS += 1

        return self.check(startS, startP + 2)
