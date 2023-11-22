# https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

from string import ascii_uppercase, ascii_lowercase


class Solution:
    def greatestLetter(self, s: str) -> str:
        c = set(list(s))
        for lower, upper in list(zip(ascii_lowercase, ascii_uppercase))[::-1]:
            if lower in c and upper in c:
                return upper
        return ''
