# https://leetcode.com/problems/shuffle-an-array/

from random import randint


class Solution:

    def __init__(self, nums: List[int]):
        self.origin = nums[:]
        self.nums = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.origin

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.nums)):
            j = randint(i, len(self.nums) - 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
