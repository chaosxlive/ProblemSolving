# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

from collections import Counter


class Solution:

    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        cnts = sorted(c.values(), reverse=True)
        result = 0
        for i, cnt in enumerate(cnts):
            if i < 8:
                result += cnt
            elif i < 16:
                result += cnt * 2
            elif i < 24:
                result += cnt * 3
            else:
                result += cnt * 4
        return result
