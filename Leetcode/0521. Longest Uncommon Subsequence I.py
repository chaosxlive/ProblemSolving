# https://leetcode.com/problems/longest-uncommon-subsequence-i/

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        if len(a) == len(b):
            return len(a)
        return max(len(a), len(b))
