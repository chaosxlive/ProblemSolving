# https://leetcode.com/problems/prime-in-diagonal/

from typing import List


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(n):
            if n == 2 or n == 3:
                return True
            if n < 2 or n % 2 == 0:
                return False
            if n < 9:
                return True
            if n % 3 == 0:
                return False
            r = int(n ** 0.5)
            f = 5
            while f <= r:
                if n % f == 0:
                    return False
                if n % (f + 2) == 0:
                    return False
                f += 6
            return True

        result = 0
        for i in range(len(nums)):
            if is_prime(nums[i][i]):
                result = max(result, nums[i][i])
            if is_prime(nums[i][len(nums) - i - 1]):
                result = max(result, nums[i][len(nums) - i - 1])
        return result
