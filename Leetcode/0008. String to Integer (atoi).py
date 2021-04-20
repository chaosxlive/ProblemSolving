# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        isNeg = False
        index = 0
        result = 0
        while index < len(s):
            if s[index] == '-':
                isNeg = True
                index += 1
                break
            elif s[index] == '+':
                index += 1
                break
            elif '0' <= s[index] <= '9':
                break
            elif s[index] == ' ':
                index += 1
                continue
            else:
                break
            
        
        while index < len(s) and '0' <= s[index] <= '9':
            result = result * 10 + (ord(s[index]) - 48)
            index += 1
        
        if isNeg:
            result *= -1
            return -2147483648 if result < -2147483648 else result
        return 2147483647 if result > 2147483647 else result