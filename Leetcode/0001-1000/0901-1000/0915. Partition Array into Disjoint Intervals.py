# https://leetcode.com/problems/partition-array-into-disjoint-intervals/

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        maxLeft, minRight = [nums[0]] * len(nums), [nums[-1]] * len(nums)
        for i in range(1, len(nums)):
            maxLeft[i] = max(maxLeft[i - 1], nums[i - 1])
        for i in range(len(nums) - 2, -1, -1):
            minRight[i] = min(minRight[i + 1], nums[i])
        for i in range(1, len(nums)):
            if maxLeft[i] <= minRight[i]:
                return i
