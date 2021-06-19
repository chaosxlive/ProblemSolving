# https://leetcode.com/problems/range-sum-query-mutable/
# TLE

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = [0] * (len(nums) + 1)
        self.nums[1] = nums[0]
        for i in range(1, len(nums)):
            self.nums[i + 1] = nums[i] + self.nums[i]

    def update(self, index: int, val: int) -> None:
        dif = val - (self.nums[index + 1] - self.nums[index])
        for i in range(index, len(self.nums) - 1):
            self.nums[i + 1] += dif

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right + 1] - self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
