# https://leetcode.com/problems/ransom-note/

from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = defaultdict(lambda: 0)
        for c in magazine:
            count[c] += 1
        for c in ransomNote:
            if count[c] == 0:
                return False
            count[c] -= 1
        return True
