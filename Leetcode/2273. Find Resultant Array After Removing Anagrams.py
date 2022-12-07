# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

from typing import List
from collections import Counter


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = [words[0]]
        left = 0
        right = 1
        cLeft = Counter(words[left])
        while right < len(words):
            cRight = Counter(words[right])
            if cLeft != cRight:
                result.append(words[right])
                cLeft = cRight
                left = right
            right += 1
        return result
