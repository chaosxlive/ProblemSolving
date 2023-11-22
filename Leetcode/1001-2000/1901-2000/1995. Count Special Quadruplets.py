# https://leetcode.com/problems/count-special-quadruplets/

from collections import defaultdict


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        possibles = defaultdict(list)
        for a in range(len(nums) - 3):
            for b in range(a + 1, len(nums) - 2):
                for c in range(b + 1, len(nums) - 1):
                    possibles[nums[a] + nums[b] + nums[c]].append(c)

        result = 0
        for i in range(3, len(nums)):
            for j in possibles[nums[i]]:
                if i > j:
                    result += 1
        return result
