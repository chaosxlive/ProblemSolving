# https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if (len(num1) == 1 and num1[0] == '0') or (len(num2) == 1 and num2[0] == '0'):
            return "0"
        results = []
        for i1 in range(len(num1) - 1, -1, -1):
            temp = 0
            for i2 in range(len(num2)):
                temp = temp * 10 + (ord(num1[i1]) - 48) * (ord(num2[i2]) - 48)
            results.append(temp)

        temp = 0
        for i in range(len(results) - 1, -1, -1):
            temp = temp * 10 + results[i]
        result = []
        while temp > 0:
            result.append(chr(temp % 10 + 48))
            temp //= 10
        return "".join(result[::-1])
