# https://leetcode.com/problems/implement-trie-ii-prefix-tree/

class TrieNode:
    def __init__(self):
        self.cntPrefix = 0
        self.cntEnd = 0
        self.children = [None] * 26

    def next(self, c: str) -> 'TrieNode':
        i = ord(c) - 97
        if self.children[i] == None:
            self.children[i] = TrieNode()
        return self.children[i]


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        it = self.root
        for c in word:
            it = it.next(c)
            it.cntPrefix += 1
        it.cntEnd += 1

    def countWordsEqualTo(self, word: str) -> int:
        it = self.root
        for c in word:
            it = it.next(c)
        return it.cntEnd

    def countWordsStartingWith(self, prefix: str) -> int:
        it = self.root
        for c in prefix:
            it = it.next(c)
        return it.cntPrefix

    def erase(self, word: str) -> None:
        it = self.root
        for c in word:
            it = it.next(c)
            it.cntPrefix -= 1
        it.cntEnd -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
