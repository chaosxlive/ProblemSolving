# https://leetcode.com/problems/remove-letter-to-equalize-frequency/

from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        c = Counter(word)
        f = c.most_common()
        if len(f) == 1 or f[0][1] == 1:
            return True

        # 1 is 1 and others are equal
        if f[-1][1] == 1 and f[0][1] == f[-2][1]:
            return True

        # 1 more than other by 1
        if f[1][1] != f[0][1] - 1 or f[-1][1] != f[0][1] - 1:
            return False
        return True
