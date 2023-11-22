# https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False
        index = 2
        while index * index < n:
            if not isPrime[index]:
                index += 1
                continue

            multiple = index * index
            while multiple < n:
                isPrime[multiple] = False
                multiple += index

            index += 1

        return isPrime.count(True)
