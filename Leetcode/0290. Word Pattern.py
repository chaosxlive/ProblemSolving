# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        splitted = s.split(' ')
        if len(pattern) != len(splitted):
            return False
        history = {}
        seen = set()
        for index in range(len(pattern)):
            if pattern[index] not in history:
                if splitted[index] in seen:
                    return False
                history[pattern[index]] = splitted[index]
                seen.add(splitted[index])
            else:
                if history[pattern[index]] != splitted[index]:
                    return False
        return True
