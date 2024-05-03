# https://leetcode.com/problems/count-the-number-of-special-characters-i/


class Solution:

    def numberOfSpecialChars(self, word: str) -> int:
        seen = [False] * 52
        a, A = ord('a'), ord('A')
        for c in word:
            o = ord(c)
            if c.islower():
                seen[o - a] = True
            else:
                seen[o - A + 26] = True
        res = 0
        for i in range(26):
            if seen[i] and seen[i + 26]:
                res += 1
        return res
