# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/


class Solution:

    def minimumPushes(self, word: str) -> int:
        ws = set(word)
        L = len(ws)
        if L <= 8:
            return L
        if L <= 16:
            return L + (L - 8)
        if L <= 24:
            return L + (L - 8) + (L - 16)
        return L + (L - 8) + (L - 16) + (L - 24)
