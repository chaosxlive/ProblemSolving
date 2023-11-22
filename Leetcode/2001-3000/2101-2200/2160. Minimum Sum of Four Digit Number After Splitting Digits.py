# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

class Solution:
    def minimumSum(self, num: int) -> int:
        nums = sorted(str(num))
        return int(''.join(nums[0::2])) + int(''.join(nums[1::2]))
