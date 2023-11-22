# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 100000
        for left in range(len(nums) - 2):
            center, right = left + 1, len(nums) - 1
            while center < right:
                numSum = nums[left] + nums[center] + nums[right]
                if abs(target - numSum) < abs(result - target):
                    result = numSum
                if numSum < target:
                    center += 1
                elif numSum > target:
                    right -= 1
                else:
                    return result
        return result
