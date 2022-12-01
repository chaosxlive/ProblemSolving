# https://leetcode.com/problems/unique-word-abbreviation/

from collections import defaultdict


class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.words = defaultdict(lambda: set())
        for word in dictionary:
            self.addWord(word)

    def isUnique(self, word: str) -> bool:
        abbr = self.getAbbr(word)
        if len(self.words[abbr]) == 0:
            return True
        elif len(self.words[abbr]) == 1:
            return word in self.words[abbr]
        else:
            return False

    def addWord(self, word: str):
        abbr = self.getAbbr(word)
        self.words[abbr].add(word)

    def getAbbr(self, word):
        return word if len(word) < 3 else word[0] + str(len(word) - 2) + word[-1]


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
