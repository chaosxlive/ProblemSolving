# https://leetcode.com/problems/maximum-prime-difference/

from typing import List

PRIME_LEN = 100
IS_PRIME = [True] * (PRIME_LEN + 1)
PRIMES = []
IS_PRIME[0] = False
IS_PRIME[1] = False
for i in range(2, PRIME_LEN + 1):
    if IS_PRIME[i]:
        PRIMES.append(i)
    j = 0
    while i * PRIMES[j] <= PRIME_LEN:
        IS_PRIME[i * PRIMES[j]] = False
        if i % PRIMES[j] == 0:
            break
        j += 1


class Solution:

    def maximumPrimeDifference(self, nums: List[int]) -> int:
        L = len(nums)
        left = 0
        while left < L and not IS_PRIME[nums[left]]:
            left += 1
        right = L - 1
        while right >= 0 and not IS_PRIME[nums[right]]:
            right -= 1
        return right - left if right >= left else 0
