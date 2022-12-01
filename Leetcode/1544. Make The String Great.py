# https://leetcode.com/problems/make-the-string-great/

class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) < 2:
            return s

        def isSame(c1, c2):
            o1 = ord(c1)
            o2 = ord(c2)
            return abs(o1 - o2) == 32

        isModified = False
        chars = list(s)

        for i in range(len(chars) - 1):
            if chars[i] != '' and chars[i + 1] != '' and isSame(chars[i], chars[i + 1]):
                chars[i] = chars[i + 1] = ''
                isModified = True

        result = ''.join(chars)

        return self.makeGood(result) if isModified else result
