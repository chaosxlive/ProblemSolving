# https://leetcode.com/problems/binary-prefix-divisible-by-5/

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        current = 0
        result = [False] * len(nums)
        for index in range(len(nums)):
            current = (current << 1) + nums[index]
            if current % 5 == 0:
                result[index] = True
        return result
