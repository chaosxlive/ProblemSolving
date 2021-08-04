# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        buffer = []
        for c in s:
            buffer.append(ord(c) - 96)
        tempSum = 0
        for n in buffer:
            temp = n
            while temp > 0:
                tempSum += temp % 10
                temp //= 10
        for times in range(1, k):
            temp = tempSum
            tempSum = 0
            while temp > 0:
                tempSum += temp % 10
                temp //= 10
        return tempSum
