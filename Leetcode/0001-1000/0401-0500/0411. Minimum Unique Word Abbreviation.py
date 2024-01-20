# https://leetcode.com/problems/minimum-unique-word-abbreviation/

from collections import defaultdict
from typing import List


class Solution:

    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        TL = len(target)
        dictionary = list(filter(lambda x: len(x) == TL, dictionary))

        def getAbbrs(word: str) -> List[str | int]:
            L = len(word)
            abbrs = []
            for i in range(2**L):
                abbr = []
                prev = 0
                for j in range(L):
                    m = 1 << j
                    if i & m:
                        if j != prev:
                            abbr.append(j - prev)
                        prev = j + 1
                        abbr.append(word[j])
                if prev != L:
                    abbr.append(L - prev)
                abbrs.append(abbr)
            return abbrs

        tgtAbbrs = sorted(getAbbrs(target), key=lambda x: len(x))

        def isMatched(abbr: List[str | int], word: str) -> bool:
            i = j = 0
            while i < len(abbr) and j < len(word):
                if isinstance(abbr[i], int):
                    j += abbr[i]
                else:
                    if abbr[i] != word[j]:
                        return False
                    j += 1
                i += 1
            return i == len(abbr) and j == len(word)

        for abbr in tgtAbbrs:
            isValid = True
            for word in dictionary:
                if isMatched(abbr, word):
                    isValid = False
                    break
            if isValid:
                return ''.join(map(lambda x: str(x) if isinstance(x, int) else x, abbr))
        return target
