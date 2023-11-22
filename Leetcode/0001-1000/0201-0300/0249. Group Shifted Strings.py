# https://leetcode.com/problems/group-shifted-strings/

from collections import defaultdict


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        ordA = ord('a')
        c = defaultdict(lambda: [])
        for s in strings:
            bias = ord(s[0]) - ordA
            nums = tuple(map(lambda x: ord(x) - bias if ord(x) - bias >= 97 else ord(x) - bias + 26, s))
            c[nums].append(s)
        return list(c.values())
