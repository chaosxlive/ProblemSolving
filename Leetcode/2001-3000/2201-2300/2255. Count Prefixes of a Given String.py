# https://leetcode.com/problems/count-prefixes-of-a-given-string/

from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return len(list(filter(lambda w: s.startswith(w), words)))
