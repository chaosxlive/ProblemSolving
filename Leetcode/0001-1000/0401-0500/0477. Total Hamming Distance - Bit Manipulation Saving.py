# https://leetcode.com/problems/total-hamming-distance/

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        count1 = [0] * 32
        maxBit = 0
        for num in nums:
            bit = 0
            while num > 0:
                if num & 1 == 1:
                    count1[bit] += 1
                maxBit = max(maxBit, bit)
                num >>= 1
                bit += 1
        result = 0
        for i in range(maxBit + 1):
            result += (len(nums) - count1[i]) * count1[i]
        return result
