# https://leetcode.com/problems/sum-of-all-subset-xor-totals/submissions/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.nums = nums
        self.result = 0

        def dfs(index, sum):
            if index == len(self.nums):
                self.result += sum
                return
            dfs(index + 1, self.nums[index] ^ sum)
            dfs(index + 1, sum)
        dfs(0, 0)
        return self.result
