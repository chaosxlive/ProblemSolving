# https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def mapWord(word):
            result = []
            count = 1
            history = {}
            for c in word:
                if c not in history:
                    history[c] = count
                    count += 1
                result.append(history[c])
            return result

        result = []
        target = mapWord(pattern)
        for word in words:
            if mapWord(word) == target:
                result.append(word)
        return result