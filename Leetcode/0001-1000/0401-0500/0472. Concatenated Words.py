# https://leetcode.com/problems/concatenated-words/

from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        result = []
        self.allWords = set(words)
        for word in words:
            self.allWords.remove(word)
            if self.check(word) is True:
                result.append(word)
            self.allWords.add(word)
        return result

    def check(self, word):
        if word in self.allWords:
            return True

        for i in range(len(word), 0, -1):
            if word[:i] in self.allWords and self.check(word[i:]):
                return True
        return False
