# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        self.left, self.right = 100000, -1

        self.search(0, len(nums))

        return [-1, -1] if self.right == -1 else [self.left, self.right]

    def search(self, left, right):
        if left >= right:
            return

        center = (left + right) // 2

        if self.nums[center] == self.target:
            if center < self.left:
                self.left = center
            if center > self.right:
                self.right = center

            if left < self.left:
                self.search(left, center)
            if right > self.right:
                self.search(center + 1, right)
        elif self.nums[center] > self.target:
            self.search(left, center)
        else:
            self.search(center + 1, right)
