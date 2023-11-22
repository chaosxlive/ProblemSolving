# https://leetcode.com/problems/repeated-substring-pattern/

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for l in range(1, len(s) // 2 + 1):
            if len(s) % l == 0:
                isSame = True
                for i in range(1, len(s) // l):
                    if s[:l] != s[l * i:l * i + l]:
                        isSame = False
                        break
                if isSame:
                    return True
        return False
