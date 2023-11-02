# https://leetcode.com/problems/split-strings-by-separator/

from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return list(w for word in words for w in word.split(separator) if len(w) > 0)
