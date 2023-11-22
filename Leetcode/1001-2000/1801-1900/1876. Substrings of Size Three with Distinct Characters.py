# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        result = 0
        for i in range(2, len(s)):
            if not (s[i] == s[i - 1] or s[i] == s[i - 2] or s[i - 1] == s[i - 2]):
                result += 1
        return result