# https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

import math


class Solution:

    def minimumDeletions(self, word: str, k: int) -> int:
        cs = [0] * 26
        for c in word:
            cs[ord(c) - ord('a')] += 1
        result = math.inf
        q = sorted(set(cs))
        for target in q:
            if target == 0:
                continue
            temp = 0
            for c in cs:
                if c < target:
                    temp += c
                elif c > target + k:
                    temp += c - target - k
            result = min(result, temp)
        return result
