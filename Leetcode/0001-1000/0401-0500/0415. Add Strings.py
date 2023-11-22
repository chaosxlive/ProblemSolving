# https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        i1, i2, carry = len(num1) - 1, len(num2) - 1, 0
        while i1 >= 0 and i2 >= 0:
            temp = ord(num1[i1]) + ord(num2[i2]) - 96 + carry
            carry = temp // 10
            result.append(chr(temp % 10 + 48))
            i1 -= 1
            i2 -= 1
        while i1 >= 0:
            temp = ord(num1[i1]) - 48 + carry
            carry = temp // 10
            result.append(chr(temp % 10 + 48))
            i1 -= 1
        while i2 >= 0:
            temp = ord(num2[i2]) - 48 + carry
            carry = temp // 10
            result.append(chr(temp % 10 + 48))
            i2 -= 1
        if carry != 0:
            result.append("1")
        return "".join(result[::-1])
