# https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/

from itertools import pairwise


class Solution:

    def isSubstringPresent(self, s: str) -> bool:
        return any(s.find(b + a) >= 0 for a, b in pairwise(s))
