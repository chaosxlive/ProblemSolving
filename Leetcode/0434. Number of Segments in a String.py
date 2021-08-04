# https://leetcode.com/problems/number-of-segments-in-a-string/

class Solution:
    def countSegments(self, s: str) -> int:
        return len([p for p in s.split(' ') if len(p) > 0])
