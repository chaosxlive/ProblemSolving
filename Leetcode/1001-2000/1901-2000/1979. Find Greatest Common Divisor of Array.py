# https://leetcode.com/problems/find-greatest-common-divisor-of-array/

from math import gcd


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxNum, minNum = 0, 1001
        for num in nums:
            maxNum = max(maxNum, num)
            minNum = min(minNum, num)

        return gcd(maxNum, minNum)
