# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            temp = 0
            while n > 0:
                temp += (n % 10) * (n % 10)
                n //= 10
            n = temp
        return True
        