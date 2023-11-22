# https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        counter = 0
        for index in range(len(nums)):
            if nums[index] == 1:
                counter += 1
            else:
                if counter > result:
                    result = counter
                counter = 0
        if counter > result:
            result = counter

        return result
