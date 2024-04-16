# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

from typing import List


class Solution:

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        seen = set()
        for n in arr1:
            s = str(n)
            t = ''
            for c in s:
                t += c
                seen.add(t)
        result = 0
        for n in arr2:
            s = str(n)
            if len(s) <= result:
                continue
            t = s[:result]
            for c in s[result:]:
                t += c
                if t in seen:
                    result = len(t)
        return result
