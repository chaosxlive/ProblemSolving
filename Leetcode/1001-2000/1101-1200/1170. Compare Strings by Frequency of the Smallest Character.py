# https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

from typing import List
from collections import Counter
from bisect import bisect_left


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        def f(s):
            c = Counter(s)
            return c[min(c.keys())]

        qs = list(map(f, queries))
        ws = sorted(map(f, words))
        return list(map(lambda x: len(ws) - bisect_left(ws, x + 1), qs))
