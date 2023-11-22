# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ptrS = ptrT = 0
        while ptrS < len(s) and ptrT < len(t):
            if s[ptrS] == t[ptrT]:
                ptrT += 1
            ptrS += 1
        return len(t) - ptrT
