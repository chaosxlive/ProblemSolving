# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        index = s.find(part)
        if index == -1:
            return s
        return self.removeOccurrences(s[:index] + s[index + len(part):], part)
