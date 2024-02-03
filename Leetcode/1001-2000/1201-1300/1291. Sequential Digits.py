# https://leetcode.com/problems/sequential-digits/

from typing import List


class Solution:

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        NUMS = '123456789'
        for l in range(1, 10):
            for i in range(10 - l):
                n = int(NUMS[i:i + l])
                if low <= n <= high:
                    result.append(n)
        return result
