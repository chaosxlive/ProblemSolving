# https://leetcode.com/problems/sign-of-the-product-of-an-array/

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        cntNeg = 0
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                cntNeg += 1
        return 1 if cntNeg % 2 == 0 else -1
