# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = set([2, 3, 5, 7, 11, 13, 17, 19])
        bits = [0] * (right + 1)
        top = 1
        bias = 1
        for i in range(1, right + 1):
            bits[i] = bits[i - bias] + 1
            if i == top:
                top = 2 * top + 1
                bias *= 2
        result = 0
        for i in range(left, right + 1):
            if bits[i] in primes:
                result += 1
        return result
