# https://leetcode.com/problems/count-pairs-of-similar-strings/

from typing import List
from collections import defaultdict


class Solution:
    def similarPairs(self, words: List[str]) -> int:

        def getCharMapBits(word: str) -> int:
            result = 0
            for c in word:
                result |= 1 << (ord(c) - 97)
            return result

        cnts = defaultdict(int)

        for word in words:
            cnts[getCharMapBits(word)] += 1

        result = 0
        for cnt in cnts.values():
            result += cnt * (cnt - 1) // 2
        return result
