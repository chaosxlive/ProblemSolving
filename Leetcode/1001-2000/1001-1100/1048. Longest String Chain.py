# https://leetcode.com/problems/longest-string-chain/

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        history = {}
        for word in words:
            prevCount = 0
            for i in range(len(word)):
                temp = word[:i] + word[i + 1:]
                if temp in history and history[temp] > prevCount:
                    prevCount = history[temp]
            history[word] = prevCount + 1
        return max(history.values())
