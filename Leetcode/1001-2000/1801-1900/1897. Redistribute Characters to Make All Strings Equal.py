# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

from collections import defaultdict


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = defaultdict(lambda: 0)
        for word in words:
            for c in word:
                count[c] += 1
        for c in count.values():
            if c % len(words) != 0:
                return False
        return True
