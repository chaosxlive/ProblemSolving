# https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/

class Solution:
    def countLetters(self, s: str) -> int:
        prevChar = s[0]
        l = 0
        idx = 0
        result = 0
        while idx < len(s):
            while idx < len(s) and s[idx] == prevChar:
                l += 1
                idx += 1
            result += (1 + l) * l // 2
            l = 0
            if idx < len(s):
                prevChar = s[idx]
        return result
