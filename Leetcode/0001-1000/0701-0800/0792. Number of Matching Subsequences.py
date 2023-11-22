# https://leetcode.com/problems/number-of-matching-subsequences/

from collections import defaultdict
import bisect


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = defaultdict(list)
        for i in range(len(s)):
            count[s[i]].append(i)

        def checkSubSeq(count, word):
            prev = -1
            for c in word:
                prev = bisect.bisect(count[c], prev)
                if prev == len(count[c]):
                    return False
                prev = count[c][prev]
            return True

        result = 0
        for word in words:
            if checkSubSeq(count, word):
                result += 1
        return result
