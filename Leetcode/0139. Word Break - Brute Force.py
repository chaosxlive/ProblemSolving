# https://leetcode.com/problems/word-break/

from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = defaultdict(lambda: [])
        for word in wordDict:
            words[word[0]].append(word)

        def find(index: int):
            if index == len(s):
                return True
            for word in words[s[index]]:
                if word == s[index:index + len(word)] and find(index + len(word)):
                    return True
            return False
        
        return find(0)

# TLE