# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

from collections import defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:
        for l in range(len(s) - 2, 0, -1):
            cnts = defaultdict(int)
            for i in range(len(s) - l + 1):
                isValid = True
                for j in range(i + 1, i + l):
                    if s[j] != s[i]:
                        isValid = False
                        break
                if isValid:
                    cnts[s[i:i + l]] += 1
            print(cnts)
            for cnt in cnts.values():
                if cnt >= 3:
                    return l
        return -1
