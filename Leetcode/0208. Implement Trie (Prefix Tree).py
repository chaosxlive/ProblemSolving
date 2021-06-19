# https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:

    class TreeNode:

        def __init__(self):
            self.next = {}
            self.isEnd = False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = self.TreeNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        ptr = self.tree
        for c in word:
            if c not in ptr.next:
                ptr.next[c] = self.TreeNode()
            ptr = ptr.next[c]
        ptr.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        def dfs(word, index, ptr):
            if index == len(word):
                return ptr.isEnd
            if word[index] in ptr.next and dfs(word, index + 1, ptr.next[word[index]]):
                return True
            return False

        return dfs(word, 0, self.tree)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        def dfs(word, index, ptr):
            if index == len(word):
                return True
            if word[index] in ptr.next and dfs(word, index + 1, ptr.next[word[index]]):
                return True
            return False

        return dfs(prefix, 0, self.tree)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
