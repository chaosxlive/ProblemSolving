# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        return self.binarySearch(0, len(nums))

    def binarySearch(self, left, right):
        if left == right:
            return -1
        center = (left + right) // 2
        if self.nums[center] == self.target:
            return center
        elif self.nums[center] > self.target:
            return self.binarySearch(left, center)
        else:
            return self.binarySearch(center + 1, right)
