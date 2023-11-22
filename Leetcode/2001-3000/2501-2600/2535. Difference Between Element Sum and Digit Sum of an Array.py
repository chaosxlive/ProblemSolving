# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum = 0
        digitSum = 0
        for num in nums:
            elementSum += num
            while num > 0:
                digitSum += num % 10
                num //= 10
        return elementSum - digitSum
