# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class WordDictionary:

    class TreeNode:

        def __init__(self):
            self.next = {}
            self.isEnd = False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = self.TreeNode()

    def addWord(self, word: str) -> None:
        ptr = self.tree
        for c in word:
            if c not in ptr.next:
                ptr.next[c] = self.TreeNode()
            ptr = ptr.next[c]
        ptr.isEnd = True

    def search(self, word: str) -> bool:

        def dfs(word, index, ptr):
            if index == len(word):
                return ptr.isEnd
            if word[index] == '.':
                for next in ptr.next.values():
                    if dfs(word, index + 1, next):
                        return True
            else:
                if word[index] in ptr.next and dfs(word, index + 1, ptr.next[word[index]]):
                    return True
            return False

        return dfs(word, 0, self.tree)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
