# https://leetcode.com/problems/count-the-number-of-special-characters-ii/


class Solution:

    def numberOfSpecialChars(self, word: str) -> int:
        seen = [0] * 26
        a, A = ord('a'), ord('A')
        for c in word:
            o = ord(c)
            if c.islower():
                if seen[o - a] == 0:
                    seen[o - a] = 1
                elif seen[o - a] == 2:
                    seen[o - a] = -1
            else:
                if seen[o - A] == 0:
                    seen[o - A] = -1
                elif seen[o - A] == 1:
                    seen[o - A] = 2
        res = 0
        for i in range(26):
            if seen[i] == 2:
                res += 1
        return res
