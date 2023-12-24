# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.vs = [(i, n) for i, n in enumerate(nums) if n > 0]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum(vec.nums[i] * n for i, n in self.vs)

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
