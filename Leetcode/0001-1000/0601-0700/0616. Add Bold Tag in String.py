# https://leetcode.com/problems/add-bold-tag-in-string/

from typing import List


class Solution:

    def addBoldTag(self, s: str, words: List[str]) -> str:

        def find_all(text, pattern):
            pattern = list(pattern)
            sfts = [1] * (len(pattern) + 1)
            sft = 1
            for pos in range(len(pattern)):
                while sft <= pos and pattern[pos] != pattern[pos - sft]:
                    sft += sfts[pos - sft]
                sfts[pos + 1] = sft
            start = 0
            mL = 0
            for c in text:
                while mL == len(pattern) or mL >= 0 and pattern[mL] != c:
                    start += sfts[mL]
                    mL -= sfts[mL]
                mL += 1
                if mL == len(pattern):
                    yield start
            return mL

        marks = [0] * len(s)
        for word in words:
            for i in find_all(s, word):
                marks[i] = max(marks[i], len(word))
        result = ''
        k = 0
        isBold = False
        for i, c in enumerate(s):
            l = marks[i]
            if k == 0:
                if l > 0:
                    if not isBold:
                        result += '<b>'
                    result += c
                    isBold = True
                    k = l - 1
                else:
                    if isBold:
                        result += '</b>'
                        isBold = False
                    result += c
            else:
                result += c
                k = max(k - 1, l - 1)
        if isBold:
            result += '</b>'
        return result
