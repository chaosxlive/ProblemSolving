# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.result = []

        self.generate(0, [])

        return self.result
    
    def generate(self, index, picked):
        if index == len(self.nums):
            self.result.append(picked[:])
            return

        self.generate(index + 1, picked + [self.nums[index]])
        self.generate(index + 1, picked)