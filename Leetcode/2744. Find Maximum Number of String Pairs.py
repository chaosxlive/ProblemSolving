# https://leetcode.com/problems/find-maximum-number-of-string-pairs/

from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        result = 0
        ws = set(words)
        for w in words:
            r = str(w[::-1])
            if r == w:
                continue
            if r in ws:
                result += 1
                ws.remove(w)
                ws.remove(r)
        return result
