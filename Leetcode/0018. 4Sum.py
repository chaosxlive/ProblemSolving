# https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        history = {n: i for i, n in enumerate(nums)}
        result = []
        seen = set()
        for a in range(len(nums) - 2):
            for b in range(a + 1, len(nums) - 1):
                for c in range(b + 1, len(nums)):
                    if target - nums[a] - nums[b] - nums[c] in history and history[target - nums[a] - nums[b] - nums[c]] > c:
                        temp = [nums[a], nums[b], nums[c], nums[history[target - nums[a] - nums[b] - nums[c]]]]
                        temp.sort()
                        if tuple(temp) not in seen:
                            seen.add(tuple(temp))
                            result.append(temp)
        return result
