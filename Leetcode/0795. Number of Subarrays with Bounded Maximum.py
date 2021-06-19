# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ptrL, ptrR = -1, -1
        result = 0
        for index, num in enumerate(nums):
            if num >= left:
                ptrR = index
            if num > right:
                ptrL = index
            result += ptrR - ptrL
        return result
