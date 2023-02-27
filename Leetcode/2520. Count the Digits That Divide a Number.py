# https://leetcode.com/problems/count-the-digits-that-divide-a-number/

class Solution:
    def countDigits(self, num: int) -> int:
        n = num
        result = 0
        while n > 0:
            if num % (n % 10) == 0:
                result += 1
            n //= 10
        return result