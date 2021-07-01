# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        def dfs(nums, used, current, result):
            if len(current) == len(nums):
                result.append(current[:])
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    current.append(nums[i])
                    dfs(nums, used, current, result)
                    current.pop()
                    used[i] = False

        dfs(nums, [False] * len(nums), [], result)
        return result
