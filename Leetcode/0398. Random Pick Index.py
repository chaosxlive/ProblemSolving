# https://leetcode.com/problems/random-pick-index/

from collections import defaultdict
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = defaultdict(list)
        for i in range(len(nums)):
            self.nums[nums[i]].append(i)

    def pick(self, target: int) -> int:
        indices = self.nums[target]
        return indices[random.randint(0, len(indices) - 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
