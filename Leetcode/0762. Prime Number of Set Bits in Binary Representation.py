# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        result = 0
        for i in range(left, right + 1):
            bitCount = bin(i).count('1')
            if bitCount in primes:
                result += 1
        return result
