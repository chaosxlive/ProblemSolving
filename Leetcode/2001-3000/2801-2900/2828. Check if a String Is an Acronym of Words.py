# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return s == ''.join(map(lambda x: x[0], words))
