# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s = 0
        l = 0
        for num in nums:
            if num % 2 == 0 and num % 3 == 0:
                s += num
                l += 1
        return s // l if l > 0 else 0
