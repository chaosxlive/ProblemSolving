# https://leetcode.com/problems/prefix-and-suffix-search/

class WordFilter:
    class TreeNode:
        def __init__(self):
            self.next = {}
            self.indice = []

    def __init__(self, words: List[str]):
        self.prefixTree = self.TreeNode()
        self.suffixTree = self.TreeNode()

        for indexWords in range(len(words)):
            word = words[indexWords]
            ptrPrefix = self.prefixTree
            ptrSuffix = self.suffixTree
            for indexWord in range(len(word)):
                if word[indexWord] not in ptrPrefix.next:
                    ptrPrefix.next[word[indexWord]] = self.TreeNode()
                ptrPrefix = ptrPrefix.next[word[indexWord]]
                ptrPrefix
                ptrPrefix.indice.append(indexWords)

                if word[-1 - indexWord] not in ptrSuffix.next:
                    ptrSuffix.next[word[-1 - indexWord]] = self.TreeNode()
                ptrSuffix = ptrSuffix.next[word[-1 - indexWord]]
                ptrSuffix.indice.append(indexWords)

    def f(self, prefix: str, suffix: str) -> int:
        ptrPrefix = self.prefixTree
        for c in prefix:
            if c not in ptrPrefix.next:
                return -1
            ptrPrefix = ptrPrefix.next[c]
        ptrSuffix = self.suffixTree
        for c in suffix[::-1]:
            if c not in ptrSuffix.next:
                return -1
            ptrSuffix = ptrSuffix.next[c]

        indexPrefix = len(ptrPrefix.indice) - 1
        indexSuffix = len(ptrSuffix.indice) - 1

        while indexPrefix >= 0 and indexSuffix >= 0:
            if ptrPrefix.indice[indexPrefix] == ptrSuffix.indice[indexSuffix]:
                return ptrPrefix.indice[indexPrefix]
            elif ptrPrefix.indice[indexPrefix] > ptrSuffix.indice[indexSuffix]:
                indexPrefix -= 1
            else:
                indexSuffix -= 1
        return -1

        # Your WordFilter object will be instantiated and called as such:
        # obj = WordFilter(words)
        # param_1 = obj.f(prefix,suffix)
