# https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        result = set()

        def dfs(nums, used, current, result):
            if len(current) == len(nums) and tuple(current) not in result:
                result.add(tuple(current))
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    current.append(nums[i])
                    dfs(nums, used, current, result)
                    current.pop()
                    used[i] = False

        dfs(nums, [False] * len(nums), [], result)
        return list(result)
