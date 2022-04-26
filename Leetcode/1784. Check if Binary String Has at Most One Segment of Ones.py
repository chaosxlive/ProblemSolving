# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        index = 0
        while index < len(s) and s[index] == '1':
            index += 1
        while index < len(s) and s[index] == '0':
            index += 1
        return index == len(s)
