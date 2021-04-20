# https://leetcode.com/problems/reverse-string-ii/

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        index = 0
        isRev = True
        result = ""
        while True:
            if index + k <= len(s):
                if isRev:
                    result += s[index + k - 1:(index - 1 if index - 1 >= 0 else None): -1]
                else:
                    result += s[index:index + k]
                isRev = not isRev
                index += k
            else:
                if isRev:
                    result += s[-1:(index - 1 if index - 1 >= 0 else None): -1]
                else:
                    result += s[index:]
                break
        return result
