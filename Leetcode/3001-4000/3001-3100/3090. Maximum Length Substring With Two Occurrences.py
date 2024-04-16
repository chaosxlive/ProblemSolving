# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

from collections import defaultdict


class Solution:

    def maximumLengthSubstring(self, s: str) -> int:
        result = 0
        for l in range(1, len(s) + 1):
            for i in range(len(s) - l + 1):
                t = s[i:i + l]
                seen = defaultdict(int)
                isValid = True
                for c in t:
                    seen[c] += 1
                    if seen[c] > 2:
                        isValid = False
                        break
                if isValid:
                    result = max(result, l)
        return result
