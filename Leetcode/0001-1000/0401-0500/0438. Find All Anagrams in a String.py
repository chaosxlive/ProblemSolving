# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        counterCurrent = Counter(s[:len(p) - 1])
        counterP = Counter(p)
        left, right = 0, len(p) - 1
        while right < len(s):
            counterCurrent[s[right]] += 1
            if counterCurrent == counterP:
                result.append(left)
            counterCurrent[s[left]] -= 1
            right += 1
            left += 1
        return result
