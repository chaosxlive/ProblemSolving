# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.nums = sorted(nums)
        self.result = set()

        self.generate(0, [])

        return list(list(t) for t in self.result)
    
    def generate(self, index, picked):
        if index == len(self.nums):
            self.result.add(tuple(picked[:]))
            return

        self.generate(index + 1, picked + [self.nums[index]])
        self.generate(index + 1, picked)