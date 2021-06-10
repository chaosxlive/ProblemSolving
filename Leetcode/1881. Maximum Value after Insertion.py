# https://leetcode.com/problems/maximum-value-after-insertion/

class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] == '-':
            index = 1
            while index < len(n):
                if x < (ord(n[index]) - 48):
                    return n[:index] + str(x) + n[index:]
                index += 1
            return n + str(x)
        else:
            index = 0
            while index < len(n):
                if x > (ord(n[index]) - 48):
                    return n[:index] + str(x) + n[index:]
                index += 1
            return n + str(x)
