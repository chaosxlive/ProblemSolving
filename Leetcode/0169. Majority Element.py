# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority = 0
        for num in nums:
            if num != majority and count != 0:
                count -= 1
            else:
                if num != majority:
                    majority = num
                count += 1
        return majority
