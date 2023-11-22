# https://leetcode.com/problems/determine-if-two-strings-are-close/

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return tuple(sorted(Counter(word1).keys())) == tuple(sorted(Counter(word2).keys())) and tuple(sorted(Counter(word1).values())) == tuple(sorted(Counter(word2).values()))
