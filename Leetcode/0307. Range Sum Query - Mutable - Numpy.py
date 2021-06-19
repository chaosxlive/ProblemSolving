# https://leetcode.com/problems/range-sum-query-mutable/

import numpy as np


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = np.array(nums)

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return np.sum(self.nums[left:right + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
