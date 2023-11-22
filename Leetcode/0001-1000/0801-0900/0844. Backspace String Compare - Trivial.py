# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def getInput(s):
            result = []
            for c in s:
                if c == '#':
                    if len(result) > 0:
                        result.pop()
                else:
                    result.append(c)
            return ''.join(result)

        return getInput(s) == getInput(t)
