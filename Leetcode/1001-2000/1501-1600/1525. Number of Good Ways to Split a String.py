# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        rightCount = Counter(s)
        rightUnique = len(rightCount)
        leftCount = Counter()
        result = 0
        for c in s:
            leftCount.update(c)
            if rightCount[c] > 0:
                rightCount[c] -= 1
            if rightCount[c] == 0:
                rightUnique -= 1

            if rightUnique == len(leftCount):
                result += 1
        return result
