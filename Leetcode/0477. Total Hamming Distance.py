# https://leetcode.com/problems/total-hamming-distance/

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            mask = 1 << i
            count = 0
            for num in nums:
                if mask & num != 0:
                    count += 1
            result += count * (len(nums) - count)
        return result
