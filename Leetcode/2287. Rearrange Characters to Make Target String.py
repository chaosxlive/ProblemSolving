# https://leetcode.com/problems/rearrange-characters-to-make-target-string/

from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        sCounter = Counter(s)
        tCounter = Counter(target)
        return min([sCounter[k] // n for k, n in tCounter.items()])
