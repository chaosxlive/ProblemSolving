# https://leetcode.com/problems/number-of-beautiful-pairs/

from typing import List
import math


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums) - 1):
            a = nums[i]
            while a >= 10:
                a //= 10
            for j in range(i + 1, len(nums)):
                b = nums[j] % 10
                if math.gcd(a, b) == 1:
                    result += 1
        return result
