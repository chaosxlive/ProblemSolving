# https://leetcode.com/problems/product-of-array-except-self/

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCnt = 0
        products = 1
        for num in nums:
            if num == 0:
                zeroCnt += 1
            else:
                products *= num
        if zeroCnt >= 2:
            return [0] * len(nums)
        if zeroCnt == 1:
            result = [0] * len(nums)
            result[nums.index(0)] = products
            return result
        return [products // num for num in nums]
