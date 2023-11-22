# https://leetcode.com/problems/arithmetic-slices/

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        gap = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
        current = 9999
        count = 0
        result = 0

        for i in range(len(gap)):
            if gap[i] == current:
                count += 1
            else:
                current = gap[i]
                result += (count * (count + 1)) // 2
                count = 0
        result += (count * (count + 1)) // 2

        return result
