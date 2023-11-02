# https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for i in range(1, n + 1):
            b = bin(i)[2:]
            try:
                print(s.index(b))
            except:
                return False
        return True