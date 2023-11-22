# https://leetcode.com/problems/prime-arrangements/

import math


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        if n == 1:
            return 1

        def isPrime(n):
            for i in range(2, int(math.sqrt(n))+1):
                if (n % i) == 0:
                    return False
            return True

        pCnt = 0
        for i in range(2, n + 1):
            if isPrime(i):
                pCnt += 1
        return (math.factorial(pCnt) % 1000000007 * math.factorial(n - pCnt) % 1000000007) % 1000000007
