# https://leetcode.com/problems/remove-adjacent-almost-equal-characters/

class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        result = 0
        i = 1
        while i < len(word):
            if abs(ord(word[i]) - ord(word[i - 1])) <= 1:
                result += 1
                i += 1
            i += 1
        return result
