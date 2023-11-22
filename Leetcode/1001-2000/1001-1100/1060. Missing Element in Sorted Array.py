# https://leetcode.com/problems/missing-element-in-sorted-array/

from typing import List


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:

        def dfs(nums, left, right, k):
            if (nums[right] - nums[left]) - (right - left) < k:
                return nums[right] + k - ((nums[right] - nums[left]) - (right - left))
            if k == 1 and (len(nums) == 1 or nums[left + 1] != nums[left] + 1):
                return nums[left] + 1
            mid = left + (right - left) // 2
            if mid == left:
                return nums[left] + k
            leftMissingCnt = (nums[mid] - nums[left]) - (mid - left)
            if leftMissingCnt < k:
                return dfs(nums, mid, right, k - leftMissingCnt)
            return dfs(nums, left, mid - 1, k)

        return dfs(nums, 0, len(nums) - 1, k)
