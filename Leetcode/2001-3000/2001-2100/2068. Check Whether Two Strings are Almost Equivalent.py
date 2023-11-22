# https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

from collections import Counter
from string import ascii_lowercase


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        for c in ascii_lowercase:
            if abs(c1[c] - c2[c]) > 3:
                return False
        return True
