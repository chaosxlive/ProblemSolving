# https://leetcode.com/problems/implement-magic-dictionary/

from collections import defaultdict


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.container = set()
        self.source = defaultdict(set)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for indexChange in range(len(word)):
                changedWord = word[:indexChange] + '.' + word[indexChange + 1:]
                self.container.add(changedWord)
                self.source[changedWord].add(word)

    def search(self, searchWord: str) -> bool:
        for indexChange in range(len(searchWord)):
            changedWord = searchWord[:indexChange] + '.' + searchWord[indexChange + 1:]
            if changedWord in self.container and (searchWord not in self.source[changedWord] or len(self.source[changedWord]) > 1):
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
