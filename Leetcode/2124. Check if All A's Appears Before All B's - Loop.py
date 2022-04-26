# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

class Solution:
    def checkString(self, s: str) -> bool:
        index = 0
        while index < len(s):
            if s[index] == 'a':
                index += 1
            else:
                break
        while index < len(s):
            if s[index] == 'b':
                index += 1
            else:
                break
        return index == len(s)
