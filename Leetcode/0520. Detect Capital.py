# https://leetcode.com/problems/detect-capital/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if 'A' <= word[0] <= 'Z':
            if len(word) >= 2 and 'A' <= word[1] <= 'Z':
                for c in word[2:]:
                    if 'a' <= c <= 'z':
                        return False
            elif len(word) >= 2 and 'a' <= word[1] <= 'z':
                for c in word[2:]:
                    if 'A' <= c <= 'Z':
                        return False
            return True
        else:
            for c in word[1:]:
                if 'A' <= c <= 'Z':
                    return False
            return True
