# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        length = len(nums)
        for center in range(1, length - 1):
            left, right = 0, length - 1
            while left != center and right != center:
                currentSum = nums[left] + nums[center] + nums[right]
                if currentSum == 0:
                    comb = [nums[left], nums[center], nums[right]]
                    if comb not in result:
                        result.append(comb)
                    left += 1
                    right -= 1
                elif currentSum < 0:
                    left += 1
                else:
                    right -= 1
        
        return result