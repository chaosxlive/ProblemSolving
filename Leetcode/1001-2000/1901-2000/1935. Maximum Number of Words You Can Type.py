# https://leetcode.com/problems/maximum-number-of-words-you-can-type/

from collections import Counter


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        result = 0
        for word in text.split(' '):
            if not any(c in brokenLetters for c in Counter(word)):
                result += 1
        return result
