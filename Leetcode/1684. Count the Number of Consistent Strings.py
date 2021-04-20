# https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = len(words)
        for word in words:
            for c in word:
                if c not in allowed:
                    result -= 1
                    break
        return result