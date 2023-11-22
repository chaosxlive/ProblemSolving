# https://leetcode.com/problems/check-if-string-is-decomposable-into-value-equal-substrings/

class Solution:
    def isDecomposable(self, s: str) -> bool:
        prev = s[0]
        idx = 0
        isTwo = False
        l = 0
        while idx < len(s):
            while idx < len(s) and s[idx] == prev:
                idx += 1
                l += 1
            print(l)
            if l % 3 == 1:
                return False
            elif l % 3 == 2:
                if isTwo:
                    return False
                isTwo = True
            l = 0
            if idx < len(s):
                prev = s[idx]
        return isTwo
