# https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/

import math
import string


class Solution:

    def minimizeStringValue(self, s: str) -> str:
        cnts = [0] * 26
        for c in s:
            if c != '?':
                cnts[ord(c) - ord('a')] += 1
        candidates = []
        for c in s:
            if c == '?':
                MIN = math.inf
                MIN_C = ''
                for l in string.ascii_lowercase:
                    lc = cnts[ord(l) - ord('a')]
                    if lc < MIN:
                        MIN = lc
                        MIN_C = l
                cnts[ord(MIN_C) - ord('a')] += 1
                candidates.append(MIN_C)
        candidates.sort()

        ss = list(s)
        j = 0
        for i, c in enumerate(ss):
            if c == '?':
                ss[i] = candidates[j]
                j += 1
        return ''.join(ss)
